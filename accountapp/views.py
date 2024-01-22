from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class AccountCreatView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:')
    template_name = 'accountapp/create.html'
