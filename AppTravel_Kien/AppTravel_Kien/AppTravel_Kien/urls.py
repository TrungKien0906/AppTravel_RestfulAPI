from django.contrib import admin
from django.urls import path, re_path, include
from AppTravel_myapp.admin import admin_site
from rest_framework import routers
from AppTravel_myapp import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configure the schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Travel API",
        default_version='v1',
        description="APIs for TravelApp",
        contact=openapi.Contact(email="kiennguyen0906.info@gmail.com"),
        license=openapi.License(name="Nguyễn Trung Kiên @2024"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Initialize the router and register viewsets
router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('tours', views.TourViewSet, basename='tours')
router.register('news', views.NewsViewSet, basename='news')
router.register('tickets', views.TicketViewSet, basename='tickets')
router.register('users', views.UserViewSet, basename='users')
router.register('comments', views.CommentViewSet, basename='comments')
router.register('rating', views.RatingViewSet, basename='rating')
router.register('booking', views.BookingViewSet, basename='booking')

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all router URLs
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAuth2 URLs
    path('admin/', admin_site.urls),  # Custom admin site URL
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),  # Swagger JSON/YAML format
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),  # Swagger UI
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc')  # Redoc UI
]
