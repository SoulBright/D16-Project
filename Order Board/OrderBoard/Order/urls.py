from django.urls import path
from .views import *

urlpatterns = [
    path('', OrderList.as_view()),
    path('<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('add/', OrderCreate.as_view(), name='order_create'),
    path('add/', OrderCreate.as_view(), name='order_create'),
    path('<int:pk>/edit/', OrderUpdate.as_view(), name='order_update'),
    path('<int:pk>/delete/', OrderDelete.as_view(), name='order_delete'),
    path('<int:pk>/delete_comment/', CommentDelete.as_view(), name='comment_delete'),
    path('accept/<int:pk>', accept_response, name='accept'),
    path('mine/', MineOrderList.as_view(), name='mine'),
]