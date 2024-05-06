from rest_framework.routers import DefaultRouter
import shop.views as views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from flower import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'orderitem', views.OrderItemViewSet, basename='orderitem')
router.register(r'review', views.ReviewViewSet, basename='review')
router.register(r'application', views.ApplicationViewSet, basename='application')
router.register(r'delivery', views.DeliveryViewSet, basename='address')

urlpatterns = [

]
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
