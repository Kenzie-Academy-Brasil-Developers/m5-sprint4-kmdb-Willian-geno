from rest_framework import serializers
from users.serializers import UserSerializer

from review.models import Review


class CourseSerializer(serializers.ModelSerializer):
    #instructor = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"



