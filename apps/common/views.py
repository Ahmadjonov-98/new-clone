from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView

from apps.post.models import Post, Notification


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        posts = Post.objects.all()
        histories = []  # history
        ntcs = Notification.objects.filter(user=self.request.user, is_seen=False).count()
        context["posts"] =  posts
        context["histories"] =  histories
        context["ntcs"] =  ntcs
        return context
