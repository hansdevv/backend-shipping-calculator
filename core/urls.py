from django.urls import path
from .views import (
    RegisterView, ProtectedView,
    CountryListCreateView, CountryDetailView,
    CategoryListCreateView, CategoryDetailView,
    CekOngkirView, SearchDomesticDestinationView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('protected/', ProtectedView.as_view(), name='protected'),

    # Country
    path('countries/', CountryListCreateView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),

    # Category
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Cek Ongkir
    path('cek-ongkir/', CekOngkirView.as_view(), name='cek-ongkir'),

    path("search-destination", SearchDomesticDestinationView.as_view(), name='search-domestic-destination'),

]
