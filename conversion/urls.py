from django.urls import path
from . import views

app_name = 'conversion'

urlpatterns = [

	path('convert',views.convert_view,name="convert"),

]