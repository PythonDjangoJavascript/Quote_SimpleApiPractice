from rest_framework import generics

from quote_api.models import Quote
from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly
from quote_api.api.pagination import FourObjectsPagePagination


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    """Manages get list and create quote endpoints"""

    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]
    pagination_class = FourObjectsPagePagination


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Manages Quote detail api Endpoints"""

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]
