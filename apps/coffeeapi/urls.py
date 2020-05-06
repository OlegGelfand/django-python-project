from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    CoffeeInfoViewSet, BeanInfoViewSet, CoffeeInfoBeanInfo, SingleCoffeeBeanInfo, PublicBeanInfo, PublicBeanDetail,)

router = DefaultRouter()
router.register('coffeeinfo', CoffeeInfoViewSet, basename='coffeeinfo')
router.register('beaninfo', BeanInfoViewSet, basename='beaninfo')

custom_urlpatterns=[
    url(r'coffeeinfo/(?P<coffeeinfo_pk>\d+)/beaninfo$',CoffeeInfoBeanInfo.as_view(), name = 'coffeeinfo_beaninfo'),
    url(r'coffeeinfo/(?P<coffeeinfo_pk>\d+)/beaninfo/(?P<pk>\d+)$', SingleCoffeeBeanInfo.as_view(),
        name='single_bean_info'),
    url(r'public-beaninfo/$', PublicBeanInfo.as_view(), name='public_beaninfo'),
    url(r'public-beaninfo/(?P<pk>\d+)/$', PublicBeanDetail.as_view(), name='public_bean_detail'),
]
urlpatterns = router.urls
urlpatterns += custom_urlpatterns