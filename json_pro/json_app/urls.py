
from django.urls import path,include
from . import views

urlpatterns = [
   
    
    path('',views.jsonConvert,name="jsonConvert"),
    # path('submit/',views.collectData,name="collectData"),
    path('<str:endpoint>',views.show_json,name="show_json"),
]
