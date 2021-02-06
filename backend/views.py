from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from django_filters import RangeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import mixins, generics, filters

from backend.models import review, post
from backend.serializers import ReviewSerializer, PostSerializer, PostGetSerializer
from django_filters import rest_framework as filters


# GENERIC FILTERS


class ProductFilter(filters.FilterSet):
    min_cost = filters.NumberFilter(field_name="cost", lookup_expr='gte')
    max_cost = filters.NumberFilter(field_name="cost", lookup_expr='lte')

    class Meta:
        model = post
        fields = ['min_cost', 'max_cost', 'item', 'category', 'productId']


class ProductList(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item', 'category', 'productId']

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save()

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        print(self.request.user)
        serializer.save()

    def delete(self, request, id=None):
        return self.destroy(request, id)


class ProductGetList(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = post.objects.all()
    serializer_class = PostGetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)


class UserListView(generics.ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']


class ReviewList(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item', 'category', 'productId']

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save()

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        print(self.request.user)
        serializer.save()

    def delete(self, request, id=None):
        return self.destroy(request, id)


class ProductGetList(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = post.objects.all()
    serializer_class = PostGetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)


# class ReviewList(generics.GenericAPIView,
#                  mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin):
#     queryset = review.objects.all()
#     serializer_class = ReviewSerializer
#
#     serializer_class = ReviewSerializer
#     queryset = review.objects.all()
#     lookup_field = 'id'
#
#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request, id)
#         else:
#             return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def put(self, request, id=None):
#         return self.update(request, id)
#
#     def perform_update(self, serializer):
#         print(self.request.user)
#         serializer.save()
#
#     def delete(self, request, id=None):
#         return self.destroy(request, id)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
