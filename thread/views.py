from django.views.generic import ListView, DetailView, CreateView
from . import models
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm, TopicForm
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django import forms



class TopicList(ListView):
    model = models.Topic
    
    context_object_name = "topic_list"
    
    template_name = "thread.html"
    

def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/thread/list')
        else:
            params['form'] = form
    else:
        params['form'] = TopicForm()
    return render(request, 'templates/new_thread.html', params)


def list(request):
    data = models.Topic.objects.all()
    params = {'message': 'スレッド一覧', 'data':data}
    return render(request, 'templates/thread.html', params)    



def detail(request, pk):
    thread = get_object_or_404(models.Topic, pk=pk)
    
    context = {
        "thread": thread,
        "comments": models.Comment.objects.filter(target=thread.id)
    }
    return render(request, 'Topic_detail.html', context)

class CommentCreate(CreateView):
    template_name = 'comment_form.html'
    model = models.Comment
    form_class = CommentForm
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.Topic, pk=self.kwargs['pk'])
        return context