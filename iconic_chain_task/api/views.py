
from django.contrib.auth import logout
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from iconic_chain_task.api.serializers import DocumentSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User has been logged out')


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def file(request):
    new_posted_file = request.FILES['file']
    data = {
        'filename': new_posted_file,
        'user': request.user.id,
        'organization': request.user.organization.id
    }
    serializer = DocumentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
