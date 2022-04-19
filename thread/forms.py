from django import forms
from .models import Topic, Comment



class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('user', 'title')
        labels = {
            'user': 'ユーザー',
            'title': 'スレッド名'
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('target', 'created_at')
