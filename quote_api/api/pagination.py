from rest_framework.pagination import PageNumberPagination


class FourObjectsPagePagination(PageNumberPagination):
    """return four objects per page"""

    page_size = 4
