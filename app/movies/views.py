from typing import Optional

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from movies.serializers import MovieSerializer
from movies.models import Movie


class MovieViewSet(ViewSet):
    def list(self, request: Request) -> Response:
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk=Optional[int]) -> Response:
        try:
            int(pk)
            movie = Movie.objects.get(pk=pk)
        except (Movie.DoesNotExist, ValueError):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def create(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
