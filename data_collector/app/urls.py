from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('service/add', ServiceCreateView.as_view(), name="add_service"),
    path('transaction/new', TransactionCreateView.as_view(), name="new_transaction")

]