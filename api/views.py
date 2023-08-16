from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response    # Import Response from rest_framework
from rest_framework.decorators import api_view  # Decorator for API Response
from .models import Note  # Model Import
from .serializers import NoteSerializer # Import Model Serializer defined in Serializer.py file
# from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote



# Create your views here.
@api_view(['GET','POST','PUT','DELETE']) 
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# to make API's Restful
# /notes (GET) - getNotes
# /notes (POST) - create Note
# /notes/<id> (GET) - getSingleNote
# /notes/<id> (PUT) - updateNote
# /notes/<id> (DELETE) - deleteNote

# else we can create it separately and update the urls.py


# @api_view(['GET','POST'])
# def getNotes(request):
#     if request.method == 'GET':
#         return getNotesList(request)

#     if request.method == 'POST':
#         return createNote(request)
    

# @api_view(['GET','PUT','DELETE'])
# def getSingleNote(request, id): # fetches a single note with id from database
#     if request.method == 'GET':
#         return getNoteDetail(request, id)

#     if request.method == 'PUT':
#         return updateNote(request, id)

#     if request.method == 'DELETE':
#         return deleteNote(request, id)



@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleNote(request,pk):
     notes = Note.objects.get(id=pk)
     serializer = NoteSerializer(notes, many=False)
     return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')