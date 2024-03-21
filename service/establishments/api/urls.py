from django.urls import path
from .views import (EstablishmentsList, EstablishmentDetail,
                    CommentListCreate, CommentDetail, HomePageView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('establishments/', EstablishmentsList.as_view(), name='establishments'),
    path('establishment/<slug:slug>/', EstablishmentDetail.as_view(), name='establishment-detail'),
    path('establishment/<slug:slug>/comments/', CommentListCreate.as_view(), name='comment-list'),
    path('establishment/<slug:slug>/comment/<int:pk>', CommentDetail.as_view(), name='comment-detail'),
]
