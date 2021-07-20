from django.urls import path
from .views import index, html, css, javascript, frontend, backend, w3c

urlpatterns = [
    path('', index, name="index"),
    path('html', html, name="html"),
    path('css', css, name="css"),
    path('javascript', javascript, name="javascript"),
    path('frontend', frontend, name="frontend"),
    path('backend', backend, name="backend"),
    path('w3c', w3c, name="w3c"),
]