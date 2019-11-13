from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'^ability', views.AbilityViewSet)
router.register(r'^type', views.PokemonTypeViewSet)
router.register(r'^egg_group', views.EggGroupViewSet)
router.register(r'^generation', views.GenerationViewSet)
router.register(r'^region', views.RegionViewSet)
router.register(r'^pokemon', views.PokemonViewSet)

urlpatterns = []
urlpatterns += router.urls
