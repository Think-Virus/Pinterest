from django.urls import path

from commentapp.views import CommentCreateView

app_name = "commentapp"

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    # path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]
