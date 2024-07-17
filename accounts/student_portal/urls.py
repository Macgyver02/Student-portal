from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('academics/', include('academics.urls')),
    path('finance/', include('finance.urls')),
    path('registration/', include('registration.urls')),
    path('exams/', include('exams.urls')),
    path('curriculum/', include('curriculum.urls')),
]