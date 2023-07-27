from django.shortcuts import render,get_object_or_404
from .serializers import MenuItemSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem,Category
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class MenuItems(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class =  MenuItemSerializer
    ordering_fields = ['price','inventory']
    search_fields=['name','category__name']
    filterset_fields=['category']
    # def get(self,request):
    #     items = MenuItem.objects.all()
    #     paginator = PageNumberPagination()
    #     paginator.page_size=5
    #     paginated_items = paginator.paginate_queryset(items,request)
    #     serialized_items =  MenuItemSerializer(paginated_items,many=True)
    #     return paginator.get_paginated_response(serialized_items.data)
    # def post(self,request):
    #     item = MenuItemSerializer(data=request.data)
    #     item.is_valid(raise_exception=True)
    #     item.save()
    #     return Response(item.data,status.HTTP_201_CREATED)

class SingleMenuItem(viewsets.ViewSet):
    def retrieve(self,request,id):
        item = get_object_or_404(MenuItem,pk=id)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data,status.HTTP_200_OK)
    
    def update(self,request,id):
        item = get_object_or_404(MenuItem,pk=id)
        serialized_item = MenuItemSerializer(item,data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data)
    
    def partial_update(self,request,id):
        item = get_object_or_404(MenuItem,pk=id)
        serialized_item = MenuItemSerializer(item,data=request.data,partial=True)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data)
    
    def destroy(self,request,id):
        item = get_object_or_404(MenuItem,pk=id)
        item.delete()
        return Response({"message": "MenuItem Deleted Successfully!"})

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class SingleCategoryView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer