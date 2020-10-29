from django.shortcuts import render

# Create your views here.
from .models import post
from .serializers import PostSerializer
from rest_framework import generics
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter



