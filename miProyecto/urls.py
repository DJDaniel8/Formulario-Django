"""
URL configuration for miProyecto project.

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
from alumnos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('listar/', views.listar_alumnos, name='listar_alumnos'),
    path('editar/<str:alumno_carnet>/', views.editar_alumno, name='editar_alumno'),
    path('eliminar/<str:carnet>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('cantidad-alumnos-por-edad/', views.cantidad_alumnos_por_edad, name='cantidad_alumnos_por_edad'),
]
