from rest_framework import generics

from quote_api.models import Quote
from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    """Manages get list and create quote endpoints"""

    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]
