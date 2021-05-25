from django.urls.conf import path, include
from profiles_api import views
from rest_framework import routers

route = routers.DefaultRouter()
route.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(route.urls))
]