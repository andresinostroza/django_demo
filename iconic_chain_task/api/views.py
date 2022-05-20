
from django.contrib.auth import logout
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from iconic_chain_task.api.models import Document, Organization
from iconic_chain_task.api.serializers import DocumentSerializer, OrganizationSerializer


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
        'filename': new_posted_file,
        'user': request.user.id,
        'organization': request.user.organization.id
    }
    serializer = DocumentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_files(request, organization_id):
    try:
        organization = Organization.objects.get(pk=organization_id)
        documents = Document.objects.filter(organization=organization)
        serializeds_documents = DocumentSerializer(documents, many=True)
        return JsonResponse(serializeds_documents.data, safe=False)
    except Organization.DoesNotExist:
        return Response('Organization does not exist', status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_organizations(request):
    organizations = Organization.objects.all()
    serializeds_documents = OrganizationSerializer(organizations, many=True)
    return JsonResponse(serializeds_documents.data, safe=False)
