from django.urls import path,include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    
    path('server/',views.ServerView.as_view(), name='serverview'),
    path('server/<int:pk>/',views.ServerDetailView.as_view(),name='serverdetailview'),
    path('server/<int:pk>/metrics/',views.ServerMetric.as_view(),name='servermeticsview'),
    path('analytics/',views.ServerAnalytics.as_view(),name='serveranalyticsview'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('token/verify/',TokenVerifyView.as_view(),name='token_verify'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
