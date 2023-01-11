from urllib.request import Request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note
from rest_framework.parsers import JSONParser


class UserNoteView(APIView):
    def get(self, request, id):
        note = Note.objects.get(id=id)
        data = NoteSerializer(note).data
        return Response(data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def patch(self, request, id, format=None):
        note = Note.objects.get(id=id)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        note = Note.objects.get(id=id)
        note.delete()
        return Response(status=204)


class UserNotesView(APIView):

    def get(self, request, username):
        notes = Note.objects.filter(author=username)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    

    