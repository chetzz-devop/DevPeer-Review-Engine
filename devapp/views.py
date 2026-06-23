from django.shortcuts import render
from .models import Project, Review
from .serializer import Projectserializer, ReviewSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class Createproject(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = Projectserializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['title']
    filterset_fields = ['title']


class UpdateDelview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = Projectserializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


class createReview(generics.CreateAPIView):
    queryset = Review
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
