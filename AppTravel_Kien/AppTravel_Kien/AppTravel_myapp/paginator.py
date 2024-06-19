from rest_framework.pagination import PageNumberPagination


class TourPaginator(PageNumberPagination):
    page_size = 20


class NewsPaginator(PageNumberPagination):
    page_size = 10