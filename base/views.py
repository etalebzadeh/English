from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from . models import *

from django.contrib.auth.hashers import make_password




from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from . serializers import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k]= v          
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
        first_name = data['name'],
        username = data["email"],
        email = data["email"],
        password = make_password(data["password"])
    )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {"detail": "User With this email already exists"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def productsList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(["GET"])
def teachersList(request):
    teachers = User.objects.filter(is_staff=True)
    serializer = UserSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def postsList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAdminUser])
def postRegister(request):
    data = request.data
    user = request.user
    try:
        post = Post.objects.create(
        user = user,
        title = data["title"],
        category = data["category"],
        subject = data["subject"]
    )
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
    except:
        message = {"detail": "User With this email already exists"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def podcastsList(request):
    teachers = Podcast.objects.all()
    serializer = PodcastSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def quizList(request):
    teachers = Quiz.objects.all()
    serializer = QuizSerialiser(teachers, many=True)
    return Response(serializer.data)
