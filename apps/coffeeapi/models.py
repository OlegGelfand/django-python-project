from django.db import models
#Linking user
from apps.authentication.models import User

# Create your models here.
class CoffeeInfo(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #if i delete the user, delete the foreign key also
    #this owner is the owner logging into our system-
    #foreign keys alays have on_delete=models.CASCADE
    # we know that owner is a field in our db
    description = models.TextField(blank=True)
    roast_type = models.TextField(blank = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class BeanInfo (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #pointing to user in authentication so that this can now be affected by a user change/delete
    #category and recipe have a connection
    coffeeinfo = models.ForeignKey(CoffeeInfo, related_name='beans', on_delete=models.CASCADE)
    #related name ='beans" means we are now using this name instead of saying coffeeinfo, therefore we can easily see the connection between the 2 tables
    #if user deleted beaninfo, we should have the app removed

    company_name = models.CharField(max_length=100)
    description= models.TextField(blank=True)
    city_of_origin = models.TextField()
    harvested_in = models.TextField()
    company_size = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class BeanInfo(models.Model):
        owner = models.ForeignKey(User, on_delete=models.CASCADE)
        # category and recipe have a connection
        coffeeinfo = models.ForeignKey(CoffeeInfo, related_name='beans', on_delete=models.CASCADE)
        # related name ='beans" means we are now using this name instead of saying coffeeinfo, therefore we can easily see the connection between the 2 tables
        # if user deleted beaninfo, we should have the app removed

        company_name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
        city_of_origin = models.TextField()
        harvested_in = models.TextField()
        company_size = models.CharField(max_length=10)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True)
        is_public = models.BooleanField(default=False)

        def __str__(self):
            return self.name