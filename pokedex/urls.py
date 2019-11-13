from rest_framework import routers
import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'^ability', views.AbilityViewSet)
router.register(r'^type', views.PokemonTypeSerializer)
router.register(r'^egg_group', views.EggGroupSerializer)
router.register(r'^generation', views.GenerationSerializer)
router.register(r'^region', views.RegionSerializer)
router.register(r'^pokemon', views.PokemonSerializer)

urlpatterns = []
urlpatterns += router.urls
