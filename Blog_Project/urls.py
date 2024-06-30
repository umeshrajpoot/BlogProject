"""
URL configuration for Blog_Project project.

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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('singup/',views.Signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('deshboard/',views.Deshboard,name='deshboard'),
    path('addpost/',views.add_post,name='addpost'),
    path('update/<int:id>',views.update_post,name='update'),
    path('delete/<int:id>/',views.delete_post,name='delete'),

    #path('delete/', views.BlogPostDeleteView.as_view(), name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
