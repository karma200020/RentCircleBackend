from rest_framework import serializers

from backend.models import post, review

from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = [
            'item',
            'reviewer',
            'rating',
            'review'
        ]
        depth = 1


class ReviewGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = [
            'item',
            'reviewer',
            'rating',
            'review',
            'reviewId'
        ]
        depth = 2


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = [
            'owner',
            'posted_on',
            'item',
            'rating',
            'description',
            'item_count',
            'category',
            'contact_number',
            'cost',
            'contact_email',
            'long',
            'lat',
            'productId'
        ]


class PostGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = [
            'owner',
            'posted_on',
            'item',
            'rating',
            'description',
            'item_count',
            'category',
            'contact_number',
            'cost',
            'contact_email',
            'long',
            'lat',
            'productId'
        ]
        depth = 2


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    username = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user
