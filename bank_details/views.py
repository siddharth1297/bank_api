from rest_framework import generics
from .models import BankBranch
from .serializers import BankBranchSerializer
from rest_framework import permissions


class ListBankDetailsView(generics.ListAPIView):
    """
    All the bank name, ifsc, address, city, district, state
    GET bank/
    """
    serializer_class = BankBranchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return BankBranch.objects.all()


class BankDetailsIfcsView(generics.RetrieveAPIView):
    """
    Bank details, for given ifsc
    GET bank/<ifsc>
    """
    serializer_class = BankBranchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return BankBranch.objects.filter(ifsc=self.kwargs.get('pk'))


class ListBankDetailsNameCityView(generics.ListAPIView):
    """
    Bank details, for given name and city
    GET bank/<name>/<city>
    """
    serializer_class = BankBranchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        name = self.kwargs.get('name')
        city = self.kwargs.get('city')
        return BankBranch.objects.all().filter(bank_name=name).filter(city=city)
