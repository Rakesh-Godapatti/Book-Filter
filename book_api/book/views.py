from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()

        # Filter by book ID
        book_ids = self.request.query_params.getlist('book_id')
        if book_ids:
            queryset = queryset.filter(id__in=book_ids)

        # Filter by language
        languages = self.request.query_params.getlist('language')
        if languages:
            queryset = queryset.filter(language__in=languages)

        # Filter by mime-type
        mime_types = self.request.query_params.getlist('mime_type')
        if mime_types:
            queryset = queryset.filter(mime_types__contains=mime_types)

        # Filter by topic
        topics = self.request.query_params.getlist('topic')
        if topics:
            queryset = queryset.filter(subjects__icontains=topics[0]) | queryset.filter(bookshelves__icontains=topics[0])
            for topic in topics[1:]:
                queryset = queryset.filter(subjects__icontains=topic) | queryset.filter(bookshelves__icontains=topic)

        # Filter by author
        authors = self.request.query_params.getlist('author')
        if authors:
            queryset = queryset.filter(author__icontains=authors[0])
            for author in authors[1:]:
                queryset = queryset.filter(author__icontains=author)

        # Filter by title
        titles = self.request.query_params.getlist('title')
        if titles:
            queryset = queryset.filter(title__icontains=titles[0])
            for title in titles[1:]:
                queryset = queryset.filter(title__icontains=title)

        return queryset.order_by('-downloads')

