from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from user.views import *
from main.views import *
from order.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Market API",
        default_version='v1',
        description="Test Market API",
        contact=openapi.Contact("Abduvaliyev Salohiddin.      Telegram: @Dasturchi_2003 ")
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Simple JWT
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),

    # Swagger
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    # Profile
    path('register/', RegisterAPIView.as_view()),
    path('profile/', ProfileRetrieveUpdateDestroyView.as_view()),

    # Main
    path('categories/', CategoryListCreateView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveDestroyView.as_view()),

    # Order
    path('selectedProducts/', SelectedProductListCreateView.as_view()),
    path('selectedProducts/<int:pk>/', SelectedProductRetrieveUpdateDestroyAPIView.as_view()),

    path('cartItems/', CartItemListCreateView.as_view()),
    path('cartItems/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view()),

    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view()),

    path('orderItems/', OrderItemListCreateView.as_view()),
    path('orderItems/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
