from django.urls import path,include

from stock.views import ProductViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# namespace
# app_name = 'stock'
router.register(r'stock-index', ProductViewset, basename='stock-index')

# urlpatterns = [
#     path('index/<str:index_name>/', ProductViewset.as_view())
# ]
urlpatterns = router.urls