from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.utils.dateparse import parse_date

from .models import Notes, Category, Tag
from .serializers import NotesSerializer, CategorySerializer, TagSerializer
from .pagination import LargeResultsSetPagination, SmallResultsSetPagination


# Create your views here.

#class NotesListCreateView(generics.ListCreateAPIView):
#    queryset = Notes.objects.all()
#    serializer_class = NotesSerializer


class NotesListCreateView(generics.ListCreateAPIView):
    queryset = Notes.objects.all().order_by("id")
    serializer_class = NotesSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        notes = Notes.objects.all().order_by("id")

        search = self.request.GET.get("search")
        if search:
            notes = notes.filter(
                Q(title__icontains = search) | Q(content__icontains = search)
            )

        category_parameter = self.request.GET.get("category")
        if category_parameter:
            if category_parameter.isdigit():
                notes = notes.filter(category_id = int(category_parameter))
            else:
                notes = notes.filter(category__name__iexact = category_parameter)

        tags_parameter = self.request.GET.get("tags")
        if tags_parameter:
            tags_list = [x.strip() for x in tags_parameter.split(",") if x.strip()]
            if tags_list:
                if all(tag.isdigit() for tag in tags_list):
                    tag_ids = [int(tag) for tag in tags_list]
                    notes = notes.filter(tags__id__in = tag_ids).distinct()
                else:
                    notes = notes.filter(tags__name__in = tags_list).distinct()
            

        created_from = parse_date(self.request.GET.get("created_from") or "")
        created_to = parse_date(self.request.GET.get("created_to") or "")
        if created_from:
            notes = notes.filter(created_at__date__gte = created_from)
        if created_to:
            notes = notes.filter(created_at__date__lte = created_to)

        ordering = self.request.GET.get("ordering")
        allowed_ordering = {"created_at", "-created_at", "title", "-title"}
        if ordering in allowed_ordering:
            notes = notes.order_by(ordering)
        else:
            notes = notes.order_by("id")

        return notes


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


'''
class NotesList(APIView):
    def get(self, request):
        notes = Notes.objects.all().order_by('id')

        search = request.GET.get('search')
        if search:
            notes = notes.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        category_id = request.GET.get('category')
        if category_id:
            notes = notes.filter(category_id=category_id)

        tags_parameter = request.GET.get('tags')
        if tags_parameter:
            try:
                tag_ids = [int(x) for x in tags_parameter.split(',') if x.strip()]
                if tag_ids:
                    notes = notes.filter(tags__id__in=tag_ids).distinct()
            except ValueError:
                pass

        created_from = parse_date(request.GET.get('created_from') or '')
        created_to = parse_date(request.GET.get('created_to') or '')
        if created_from:
            notes = notes.filter(created_at__date__gte=created_from)
        if created_to:
            notes = notes.filter(created_at__date__lte=created_to)

        ordering = request.GET.get('ordering')
        allowed_ordering = {'created_at', '-created_at', 'title', '-title'}
        if ordering in allowed_ordering:
            notes = notes.order_by(ordering)
        else:
            notes = notes.order_by('id')

        paginator = SmallResultsSetPagination()
        page = paginator.paginate_queryset(notes, request)

        serializer = NotesSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            return None

    def get(self, request, pk):
        note = self.get_object(pk)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NotesSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk):
        note = self.get_object(pk)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NotesSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_object(pk)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagList(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''






'''
@api_view(['GET'])
def get_notes(request):
    notes = Notes.objects.all().order_by('id')

    search = request.GET.get('search')
    if search:
        notes = notes.filter(Q(title__icontains = search) | Q(content__icontains = search))

    category_id = request.GET.get('category')
    if category_id:
        notes = notes.filter(category_id = category_id)

    tags_parameter = request.GET.get('tags')
    if tags_parameter:
        try:
            tag_ids = [int(x) for x in tags_parameter.split(',') if x.strip()]
            if tag_ids:
                notes = notes.filter(tags__id__in = tag_ids).distinct()
        except ValueError:
            pass

    created_from = parse_date(request.GET.get('created_from') or '')
    created_to = parse_date(request.GET.get('created_to') or '')
    if created_from:
        notes = notes.filter(created_at__date__gte = created_from)
    if created_to:
        notes = notes.filter(created_at__date__lte = created_to)

    ordering = request.GET.get('ordering')
    allowed_ordering = {'created_at','-created_at','title','-title'}
    if ordering in allowed_ordering:
        notes = notes.order_by(ordering)
    else:
        notes = notes.order_by('id')

    paginator = SmallResultsSetPagination()
    page = paginator.paginate_queryset(notes, request)

    serializer = NotesSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

    
@api_view(['POST'])
def create_notes(request):
    serializer = NotesSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
def note_details(request, pk):
    try:
        note = Notes.objects.get(pk = pk)
    except Notes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotesSerializer(note)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = NotesSerializer(note, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        note.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''