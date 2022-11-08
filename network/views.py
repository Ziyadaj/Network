import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post, Follow, Comment

# all posts
def index(request):
    posts = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    user = request.user
    comments = Comment.objects.all().order_by('-timestamp')
    content = []
    for post in posts:
        content.append(post.content)
    return render(request, "network/index.html", {
        "page_obj": page_obj,
        "user": user,
        "comments": comments,
        "content": content
    })


# New Post
@csrf_exempt
@login_required
def form(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    if data.get("content") is not None:
        post = Post(content=data["content"], user=request.user)
        post.save()
        return JsonResponse({"message": "Post created successfully."}, status=201)
    return JsonResponse({"error": "Post content required."}, status=400)
    
# profile page
def profile(request, user_name):
    user = request.user
    profile = User.objects.get(username=user_name)
    posts = Post.objects.filter(user=profile).order_by('-timestamp')
    #limit to 5 posts
    paginator = Paginator(posts, 5)
    #ignore page number
    followers = profile.followers.all().count()
    following = profile.following.all().count()
    if not user.is_anonymous:
        followed = False
        follow_obj = Follow.objects.filter(user=user, follower=profile)
        if follow_obj.exists():
            followed = True
        return render(request, "network/profile.html", {
            "user": user,
            "profile": profile,
            "name": user_name,
            "followers": followers,
            "following": following,
            "followed": followed,
            "posts": paginator.get_page(1),
            "anonymous": False
        })
    return render(request, "network/profile.html", {
        "user": user,
        "profile": profile,
        "name": user_name,
        "posts": paginator.get_page(1),
        "followers": followers,
        "following": following,
        "anonymous": True
    })

# following page
@login_required(login_url='/login')    
def following(request):
    user = request.user
    follow_obj = Follow.objects.filter(user=user)
    if follow_obj.exists():
        following = []
        for follow in follow_obj:
            following.append(follow.follower)
        posts = Post.objects.filter(user__in=following).order_by('-timestamp')
        paginator = Paginator(posts, 10)
        page_obj = paginator.get_page(1)
        # latest ten posts
        return render(request, "network/following.html", {
            "page_obj": page_obj
        })
    return render(request, "network/following.html", {
        "page_obj": None
    })

# add a follower
@csrf_exempt
def add_following(request, user_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    user = request.user
    profile = User.objects.get(id=user_id)
    if user_id == user.id:
        return JsonResponse({"error": "Cannot follow yourself."}, status=400)
    
    follow_obj = Follow.objects.filter(user=user, follower=profile)

    ## if user is not following profile
    if not follow_obj.exists():
        # add user to following
        follow = Follow(user=user, follower=profile)
        follow.save()
        return JsonResponse({"message": "Follow successful."}, status=201)
    else:
        # remove user from following
        follow_obj.delete()
        return JsonResponse({"message": "Unfollow successful."}, status=201)

# edit a post
@csrf_exempt
def edit(request, post_id):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)
    data = json.loads(request.body)
    if data.get("content") is not None:
        post = Post.objects.get(id=post_id)
        post.content = data["content"]
        post.save()
        return JsonResponse({"message": "Post edited successfully."}, status=201)
    return JsonResponse({"message": "Post updated successfully."}, status=201)

# like a post
@csrf_exempt
def like(request, post_id):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)
    post = Post.objects.get(id=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    post.save()
    return JsonResponse({"message": "Post liked/Disliked successfully."}, status=201)

# add a comment to a post
@csrf_exempt
def comment(request, post_id):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)
    data = json.loads(request.body)
    if data.get("comments") is not None:
        post = Post.objects.get(id=post_id)
        comment = Comment(user=request.user, post=post, content=data["comments"])
        comment.save()
        return JsonResponse({"message": "Comment created successfully."}, status=201)
    return JsonResponse({"error": "Comment content required."}, status=400)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
