import imp
from django.http import JsonResponse
from .models import Question
from .serializers import QuestionsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from backend import serializers


@api_view(["GET", "POST"])
def questionList(request):

    if request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return JsonResponse({"questions": serializer.data}, safe=False)

    if request.method == "POST":
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def question_info(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = QuestionsSerializer(question)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = QuestionsSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
