from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = "commentapp"

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
    # path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
]
