from django.urls import path

from accountapp.views import AccountCreatView

app_name = "accountapp"

urlpatterns = [
    path('create/', AccountCreatView.as_view(), name='create'),
]
