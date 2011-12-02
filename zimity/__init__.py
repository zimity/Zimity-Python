from django.contrib.comments.models import Comment
from zimity.forms import SlimCommentForm

def get_model():
    return Comment

def get_form():
    return SlimCommentForm