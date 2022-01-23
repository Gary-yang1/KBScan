from django.urls import path
from . import views
# from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('result/', views.result),
]

# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.server_error