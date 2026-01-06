from rest_framework.viewsets import ModelViewSet
from .models import ContactMessage
from .serializers import ContactSerializer

class ContactViewSet(ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer

