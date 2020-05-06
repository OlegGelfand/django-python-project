from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import(ValidationError, PermissionDenied)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (CoffeeInfo, BeanInfo)
from .serializers import (
    CoffeeInfoSerializer, BeanInfoSerializer,
)

class CoffeeInfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
#get method for all coffee info
    def get_queryset(self):
        queryset = CoffeeInfo.objects.all().filter(owner=self.request.user)
        return queryset
    #handling json req
    serializer_class = CoffeeInfoSerializer

#create method for coffee info
    def create(self, request, *args, **kwargs):
        coffeeInfo = CoffeeInfo.objects.filter(
            name = request.data.get('name'),
            # request is what user is sending, data is that package from user
            owner = request.user
            #We filtered owner data into name data
        )
        if coffeeInfo:
            msg = 'coffee with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

#delete method for coffee

    def destroy(self, request, *args, **kwargs):
        coffeeinfo = CoffeeInfo.objects.get(pk=self.kwargs["pk"])
        if not request.user == coffeeinfo.owner:
            raise PermissionDenied("don't delete my coffee!")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) #saving this particular owner

class CoffeeInfoBeanInfo(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)#not only can they create but then can list
#get all coffee
    def get_queryset(self):
        if self.kwargs.get("coffeeinfo_pk"):
             coffeeinfo = CoffeeInfo.objects.get(pk=self.kwagrs["coffeeinfo_pk"])
             queryset = BeanInfo.objects.filter(
                 owner=self.request.user,
                 coffeeInfo=coffeeinfo
             )
        return queryset

    serializer_class = BeanInfoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SingleCoffeeBeanInfo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
# get beaninfo for user
    def get_queryset(self):
        if self.kwargs.get("coffeeinfo_pk") and self.kwargs.get("pk"):
            coffeeinfo = CoffeeInfo.objects.get(pk=self.kwargs["coffeeinfo_pk"])
            #now we need to filter to see the recipe particular to that user
            queryset= BeanInfo.object.filter(
                pk=self.kwargs["pk"],
                owner=self.request.user,
                coffeeinfo = coffeeinfo
            )
        return queryset
    serializer_class = BeanInfoSerializer
                # give me the primary key
            #kwargs is keyword args- list of imput that we get
class BeanInfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = BeanInfo.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = BeanInfoSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied("Clients can create bean info")
        return super().create(request,*args, *kwargs)
    def destroy(self, request, *args, **kwargs):
            beans = BeanInfo.objects.get(pk=self.kwargs["pk"])
            if not request.user == beans.owner:
                raise PermissionDenied("don't delete my beans!")
            return super().destroy(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
       beans = BeanInfo.object.get(pk=self.kwargs["pk"])
       if not request.user == BeanInfo.owner:

           raise PermissionDenied("you can't modify this bean information")
       return super().update(request, *args, *kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PublicBeanInfo(generics.ListAPIView):
    permission_classes = (AllowAny,)
    def get_queryset(self):
        queryset = BeanInfo.objects.all().filter(is_public=True)
        return queryset
    serializer_class = BeanInfoSerializer
class PublicBeanDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    def get_queryset(self):
        queryset = BeanInfo.objects.all().filter(is_public=True)
        return queryset
    serializer_class = BeanInfoSerializer