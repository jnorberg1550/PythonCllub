
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubapp/', include ('clubapp.urls')),
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getmeetings/', views.getmeetings, name='meetings')
     path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
]
