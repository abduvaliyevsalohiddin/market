from .serializers import *
from rest_framework import filters
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.views import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class CategoryListCreateView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    search_description = 'Search by name and description'
    ordering_fields = ['id', 'name']


class ProductAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="price",
                in_=openapi.IN_QUERY,
                description="Filter by Price",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                description="Filter by Category ID",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def get(self, request):
        projects = Product.objects.all()
        price = request.query_params.get('price')
        category_id = request.query_params.get('category_id')
        if price:
            projects = projects.filter(price__gte=float(price))
        if category_id:
            projects = projects.filter(category=category_id)

        serializer = ProductSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ProductSerializer,
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CommentListCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="user_id",
                in_=openapi.IN_QUERY,
                description="Filter by User ID",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="project_id",
                in_=openapi.IN_QUERY,
                description="Filter by Project ID",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def get(self, request):
        comments = Comment.objects.all()
        user_id = request.query_params.get('user_id')
        product_id = request.query_params.get('product_id')
        if product_id:
            comments = comments.filter(product__id=product_id)
        if user_id:
            comments = comments.filter(product__user__id=user_id)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentRetrieveDestroyView(RetrieveDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
