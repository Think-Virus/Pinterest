from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.forms import AccountUpdateForm


# Create your views here.
class AccountCreatView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'