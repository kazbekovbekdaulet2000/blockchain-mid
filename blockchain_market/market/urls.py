from django.urls import path, include
from market.views.order import CreateOrder, OrderList
from market.views.user_reg import CreateUserView
from .views.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('products/', ProductView.as_view()),
  path('order/', OrderList.as_view()),
  path('order/create/', CreateOrder.as_view()),
  path('blocks/', AllBlocks.as_view()),
  path('blocks/create/', CreatBlock.as_view()),
  
  
  path('sign-up/', CreateUserView.as_view()),
  path('sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('sign-in/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]