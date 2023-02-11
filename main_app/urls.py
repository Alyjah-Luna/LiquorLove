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
    path('liquors/<int:liquor_id>/add_spirit/', views.add_spirit, name='add_spirit'),
    path('liquors/<int:liquor_id>/assoc_cocktail/<int:cocktail_id>/', views.assoc_cocktail, name='assoc_cocktail'),
    path('liquors/<int:liquor_id>/unassoc_cocktail/<int:cocktail_id>/', views.unassoc_cocktail, name='unassoc_cocktail'),
]