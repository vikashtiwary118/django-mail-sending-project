from django.urls import path
#from . views import send_admin_mail
from . import views
urlpatterns=[
    
    path("sendAdminMail/",views.sendAdminMail,name="sendAdminMail"),
                                                                        
]