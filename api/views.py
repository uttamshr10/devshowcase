from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from application import models
from api import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'}
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = models.Project.objects.all()
    serializer = serializers.ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    project = models.Project.objects.get(pk=pk)
    serializer = serializers.ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = models.Project.objects.get(pk=pk)
    user = request.user.profile
    data = request.data
    review, created = models.Review.objects.get_or_create(
        owner = user,
        project = project,
    )
    review.value = data['value'] # change the review if already done previously
    review.save()
    project.getVoteCount

    serializer = serializers.ProjectSerializer(project, many=False)
    return Response(serializer.data)
