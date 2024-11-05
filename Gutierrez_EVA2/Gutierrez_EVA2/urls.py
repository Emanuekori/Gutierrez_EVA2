"""
URL configuration for Gutierrez_EVA2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from APP_EVA2 import views

urlpatterns = [
    path('', views.listar_inscripciones, name='listar_inscripciones'),
    path('agregar/', views.agregar_inscripcion, name='agregar_inscripcion'),
    path('modificar/<int:id>/', views.modificar_inscripcion, name='modificar_inscripcion'),
    path('eliminar/<int:id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]
