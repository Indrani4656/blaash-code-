"""
URL configuration for blaash_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import*


urlpatterns = [
    path('admin/', admin.site.urls),

    path('engagement-posts/<int:tenant_id>/', views.EngagementPostView.as_view()),
    path('create-product/', views.CreateProductView.as_view()),
    path('create-collection/', views.CreateCollectionView.as_view()),
    path('top-posts/<int:tenant_id>/', views.TopPostsView.as_view()),
    path('top-products/<int:tenant_id>/', views.TopProductsView.as_view()),
    path('engagement-post-collection/', views.EngagementPostCollectionView.as_view()),
    path('get-engagement-post-collection/<int:collection_id>/', views.GetEngagementPostCollectionView.as_view()),
]



