from re import search
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Entry

# Create your views here.

class journalLogIn(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('My Journal')

class journalLogOut(LogoutView):
    template_name = 'base/logout.html'
    fields = '__all__'

    def get_next_url(self):
        return reverse_lazy('login')

class journalSignUp(FormView):
    template_name = 'base/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

    success_url = reverse_lazy('My Journal')

    def form_valid(self, form):
        user = form.save()
        return super(journalSignUp, self).form_valid(form)


class entryList(LoginRequiredMixin, ListView):
    model = Entry
    context_object_name = 'entries'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['entries'] = data['entries'].filter(user = self.request.user)

        inp = self.request.GET.get('searchbox') or ''
        if inp != '':
            data['entries'] = data['entries'].filter(title__icontains= inp)

        data[inp] = inp
        return data

class entryDetail(LoginRequiredMixin, DetailView):
    model =  Entry
    context_object_name = 'entry'

class entryCreate(LoginRequiredMixin, CreateView):
    model =  Entry
    fields = ['title', 'content']
    success_url = reverse_lazy('My Journal')

    def form_valid(self, form):
        form.instance.user =  self.request.user
        return super(entryCreate, self).form_valid(form)

class entryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']
    success_url = reverse_lazy('My Journal')

class entryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    context_object_name = 'entry'
    success_url = reverse_lazy('My Journal')


     
    





