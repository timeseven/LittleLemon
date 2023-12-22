from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    # add following lines to urlpatterns list
    path('restaurant/menu/', views.MenuItemsView.as_view()),
    path('restaurant/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
