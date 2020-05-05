from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    CoffeeInfoViewSet, BeanInfoViewSet, CoffeeInfoBeanInfo, SingleCoffeeBeanInfo)

router = DefaultRouter()
router.register('coffeeinfo', CoffeeInfoViewSet, basename='coffeeinfo')
router.register('beaninfo', BeanInfoViewSet, basename='beaninfo')

custom_urlpatterns=[
    url(r'coffeeinfo/(?P<coffeeinfo_pk>\d+)/beaninfo$',CoffeeInfoBeanInfo.as_view(), name = 'coffeeinfo_beaninfo'),
    url(r'coffeeinfo/(?P<coffeeinfo_pk>\d+)/beaninfo/(?P<pk>\d+)$', SingleCoffeeBeanInfo.as_view(),
        name='single_bean_info'),
]
urlpatterns = router.urls
urlpatterns += custom_urlpatterns