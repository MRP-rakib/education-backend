# # blog/views.py
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .models import Blog
# from . import BlogSerializer

# class BlogViewSet(ModelViewSet):
#     serializer_class = BlogSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         queryset = Blog.objects.filter(is_active=True)
#         category = self.request.query_params.get('category')
#         if category:
#             queryset = queryset.filter(category=category)
#         return queryset
