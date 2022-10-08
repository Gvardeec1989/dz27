from django.urls import path

from users.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/', UserUpdateView.as_view()),
    path('delete/', UserDeleteView.as_view()),
]
