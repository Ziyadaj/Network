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
    def serialize(self): # This is a method that returns a dictionary of the object's attributes
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p"),
            "user": self.user.username,
            "likes": [user.username for user in self.likes.all()],
        }
class Follow(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    def serialize(self):
        return {
            "user": self.user.username,
            "follower": self.follower.username
        }
    def __str___(self):
        return f"{self.user} follows {self.follower}"
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "post": self.post.id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p")
        }