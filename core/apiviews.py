from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import (
    WebsiteSerializer,
)

from .models import (
    Website,
)

"""
#   This is the initial implementation
#   for the WebsiteInfo API view. But,
#   I'll need to implement API wide
#   authentication.

class WebsiteInfo(APIView):
    def get(self, request):
        website = get_object_or_404(Website)
        serializer = WebsiteSerializer(website)
        data = serializer.data
        return Response(data)
"""    


class WebsiteInfo(generics.ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
