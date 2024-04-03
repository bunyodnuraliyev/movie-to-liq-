from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from configAPP.models import Movie, Actor, Comment
from configAPP.serializers import MovieSerializer, ActorSerializer, CommentSerializer


class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(request_body=MovieSerializer)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# class M

class ActorAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(request_body=ActorSerializer)
    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ViewSet):
    def name_list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def ret_retrieve(self, request, pk):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class CommentApiVIev(APIView):
    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # @swagger_auto_schema(request_body=MovieSerializer)
    @action(detail=True, methods=['POST'])
    def add_actor(self, request, pk):
        actor = request.data['actor']
        movie = self.get_object()
        movie.actor.add(actor)
        movie.save()
        serializer = MovieSerializer(Movie)
        return Response(data=serializer.data)
