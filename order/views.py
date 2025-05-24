from .serializers import *
from rest_framework import filters
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.views import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class SelectedProductListCreateView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SelectedProductSerializer
    queryset = SelectedProduct.objects.all()


class SelectedProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SelectedProductSerializer
    queryset = SelectedProduct.objects.all()


class CartItemListCreateView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class CartItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class OrderListCreateView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemListCreateView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class ReviewListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReviewListSerializer
    queryset = Review.objects.all()


class ReviewCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()


class ReviewRetrieveAPIView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReviewListSerializer
    queryset = Review.objects.all()


class ReviewUpdateAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()


class ReviewDestroyAPIView(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
