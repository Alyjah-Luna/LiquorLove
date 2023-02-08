from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('liquors/', views.liquors_index, name='index'),
    path('liquors/<int:liquor_id>/', views.liquors_detail, name='detail'),
    path('liquors/create/', views.LiquorCreate.as_view(), name='liquors_create'),
    path('liquors/<int:pk>/update/', views.LiquorUpdate.as_view(), name='liquors_update'),
    path('liquors/<int:pk>/delete/', views.LiquorDelete.as_view(), name='liquors_delete'),
]