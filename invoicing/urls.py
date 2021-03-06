"""invoicing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import modules.core.web.urls
import modules.billing.web.urls

admin.site.site_header = "Invoicing"
admin.site.site_title = "Invoicing"
admin.site.index_title = "Invoicing"
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"api/core/", include(modules.core.web.urls.router.urls)),
    path(r"api/billing/", include(modules.billing.web.urls.router.urls)),
]
urlpatterns += staticfiles_urlpatterns()
