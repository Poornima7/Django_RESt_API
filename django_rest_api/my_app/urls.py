from django.urls import path, include

from my_app.views import MyFriend, MyFriendDetail

urlpatterns = [
    path('', MyFriend.as_view()),
    path('<int:pk>/', MyFriendDetail.as_view()),
]
