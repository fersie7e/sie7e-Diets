from django.urls import path

from . import views

urlpatterns = [
    path("<int:page>", views.index, name="index"),
    path("new/", views.nuevo_cliente, name="nuevo_cliente"),
    #path("ficha/<int:id_cliente>", views.ficha_cliente, name="ficha_cliente"),
    path("revision/<int:id_cliente>", views.ficha_revision, name="ficha_revision"),
    path("pdf_revision/<int:id_revision>", views.pdf_revision, name="pdf_revision"),
    #path("nueva_analitica/<int:id_cliente>", views.nueva_analitica, name="nueva_analitica"),
    
    path("offline/", views.offline, name="offline"),

    path("revision/data/<int:id_cliente>", views.ChartData.as_view()),
]
