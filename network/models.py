from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    comments = models.ManyToManyField(User, blank=True, related_name="comments")
    following = models.ManyToManyField(User, blank=True, related_name="following")
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    def serialize(self): # This is a method that returns a dictionary of the object's attributes
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p"),
            "user": self.user.username,
            "likes": [user.username for user in self.likes.all()],
            "comments": [user.username for user in self.comments.all()],
            "following": [user.username for user in self.following.all()],
            "followers": [user.username for user in self.followers.all()]
        }