from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from . views import *

urlpatterns = [    
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path("users/profile/", getUserProfile, name="user-profile"),
    path("users/", getUserProfile, name="users"),
    path("users/register/", registerUser, name="register"),
    path("products/", productsList, name="product-list"),
    path("products/<int:pk>", productDetail, name="product-list"),
    path("teachers/", teachersList, name="teachers"),
    path("posts/", postsList, name="posts"),
    path("posts/register",postRegister, name="post-register"),
    path("quizzes/", quizList, name="quizzes"),
    path("podcasts/", podcastsList, name="podcasts"),
]