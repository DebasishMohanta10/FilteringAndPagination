from django.urls import path
from . import views
urlpatterns = [
    path("menu-items/",views.MenuItems.as_view()),
    path("menu-items/<int:id>",views.SingleMenuItem.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path("categories/",views.CategoriesView.as_view()),
    path("categories/<int:pk>",views.SingleCategoryView.as_view()),
]