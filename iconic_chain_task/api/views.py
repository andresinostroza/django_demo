
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from iconic_chain_task.api.models import IconicFile, Organization, User
from iconic_chain_task.api.serializers import IconicFileDownloadLogSerializer, IconicFileSerializer, OrganizationSerializer, UserSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User has been logged out')


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_file(request):
    new_posted_file = request.FILES['file']
    data = {
        'file': new_posted_file,
        'user': request.user.id,
        'organization': request.user.organization.id
    }
    serialized_iconic_file = IconicFileSerializer(data=data)
    if serialized_iconic_file.is_valid():
        serialized_iconic_file.save()
        return JsonResponse(serialized_iconic_file.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_iconic_file.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_files(request, organization_id):
    try:
        organization = Organization.objects.get(pk=organization_id)
        files = IconicFile.objects.filter(organization=organization)
        serializeds_files = IconicFileSerializer(files, many=True)
        return JsonResponse(serializeds_files.data, safe=False)
    except Organization.DoesNotExist:
        return Response('Organization does not exist', status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_organizations(request):
    organizations = Organization.objects.all()
    serializeds_documents = OrganizationSerializer(organizations, many=True)
    return JsonResponse(serializeds_documents.data, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.all()
    serializeds_users = UserSerializer(users, many=True)
    return JsonResponse(serializeds_users.data, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_file(request, file_id):
    try:
        iconic_file = IconicFile.objects.get(pk=file_id)
        filename = iconic_file.file.name.split('/')[-1]
        response = HttpResponse(iconic_file.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        data = {
            'file': iconic_file.id,
            'user': request.user.id,
            'organization': request.user.organization.id
        }
        serialized_iconic_file = IconicFileDownloadLogSerializer(data=data)
        if serialized_iconic_file.is_valid():
            serialized_iconic_file.save()
            return JsonResponse(serialized_iconic_file.data, status=status.HTTP_201_CREATED)
        return response
    except IconicFile.DoesNotExist:
        return Response('File does not exist', status=status.HTTP_404_NOT_FOUND)
