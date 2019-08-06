from django.urls import path
from .views import ListBankDetailsView, ListBankDetailsNameCityView, BankDetailsIfcsView

urlpatterns = [
    path('bank/', ListBankDetailsView.as_view(), name="banks-all"),
    path('bank/<str:pk>/', BankDetailsIfcsView.as_view(), name="bank-details"),
    path('search/<str:name>-<str:city>/', ListBankDetailsNameCityView.as_view(), name="banks-detail-name-city")
]
