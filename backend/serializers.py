from dataclasses import fields
from rest_framework import serializers
from .models import Question
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id" ,"title" , "text"]