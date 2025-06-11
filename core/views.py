from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, CountrySerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Country, Category
from .utils import cek_ongkir, search_domestic_destination

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})

# --- COUNTRY ---
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

# --- CATEGORY ---
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# --- Ongkir Check ---
class CekOngkirView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        origin = request.data.get('origin')
        destination = request.data.get('destination')
        weight = request.data.get('weight')
        courier = request.data.get('courier')

        if not all([origin, destination, weight, courier]):
            return Response({'error': 'Semua field wajib diisi.'}, status=400)

        result = cek_ongkir(origin, destination, weight, courier)
        return Response(result)

class SearchDomesticDestinationView(APIView):
    def get(self, request):
        search = request.query_params.get("search")

        if not search:
            return Response({"error": "search is required"}, status=400)

        data = search_domestic_destination(search)
        return Response(data)
