from rest_framework import routers

from . import views


router = routers.SimpleRouter()

router.register(basename='', viewset=views.Activity, prefix='')
