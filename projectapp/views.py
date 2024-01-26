from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from projectapp.models import Project


# Create your views here.
class ProjectCreateView(CreateView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectListView(ListView):
    model = Project
