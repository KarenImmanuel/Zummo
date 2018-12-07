from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
app_name='music'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<int:categories_id>/', views.detail, name='detail'),
    path('all/', views.all, name='all'),
    path('api/', views.CategoriesList.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)