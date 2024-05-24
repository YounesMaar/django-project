from ynab import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
      path("admin/", admin.site.urls),
      path("", views.inscription, name='inscription'),
      path("connexion/", views.connexion, name='connexion'),
      path("acceuil/", views.acceuil, name='acceuil'),
      path('deconnexion/',views.deconnexion,name='deconnexion'),
      path('', views.index, name='index'),
      path('add_depense/', views.add_depense, name='add_depense'),
      path('add_budget/', views.add_budget, name='add_budget'),
      path('historique_depenses/', views.historique_depenses, name='historique_depenses'),
      path('historique_budgets/', views.historique_budgets, name='historique_budgets')
]

    