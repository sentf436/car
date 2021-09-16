
from django.urls import path

from review.views import *

urlpatterns = [
    path('review/', ReviewListView.as_view()),
    path('review/detail/<int:pk>/', ReviewDetailView.as_view()),
    path('review/create/', CreateReviewView.as_view()),
    path('review/update/', UpdateReviewView.as_view()),
    path('review/delete/', DeleteReviewView.as_view()),

    path('view/', ReviewViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('view/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'})),
    ]
