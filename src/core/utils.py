from rest_framework.pagination import CursorPagination


class ProductsPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'size'
