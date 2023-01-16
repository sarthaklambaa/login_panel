"""login_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from login import views as login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', login_view.home_page, name='home'),
    path('', login_view.login_page, name='login'),
    path('successful/', login_view.user_created, name = 'successful'),
    path('fail/', login_view.fail, name = 'fail'),
    path('signup/', login_view.signup_page, name='signup'),
    path('logout/', login_view.logout_page, name='logout'),
    path('username_taken/', login_view.username_taken, name='username_taken'),
    path('password_error/', login_view.password_error, name='password_error'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)