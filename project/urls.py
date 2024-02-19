"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from feedback import views
from django.urls import include, path

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home),
   	path('student_login/',views.student_login),
   	path('teacher_login/',views.teacher_login),
	path('student_login/register/',views.student_form_view),
	path('student_login/login/',views.student_login_view),
    path('feedback_formCSN209/',views.feedbackCSN209),
	path('feedback_formCSN211/', views.feedbackCSN211),
	path('feedback_resultCSN209/',views.feedback_resultCSN209),
	path('feedback_resultCSN211/',views.feedback_resultCSN211),
	path('change_password/',views.changepassword)


]
