from django.core import signing
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import viewsets, permissions, parsers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer, SimpleUserSerializer
from api.permissions import IsUnauthenticated

User = get_user_model()

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    page_size = 10

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return SimpleUserSerializer
        else:
            return self.serializer_class

class RegistrationView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (
        permissions.AllowAny,
        IsUnauthenticated
    )
    renderer_classes = (JSONRenderer,)
    authentication_classes = ()

    def create_user(self, data):
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def post(self, request):
        user = self.create_user(request.data)
        created_user_serializer = UserSerializer(user)

        response = {
            'user': created_user_serializer.data,
            'token': user.token,
        }

        return Response(response, status=status.HTTP_201_CREATED)
