from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = []
urlpatterns += router.urls
