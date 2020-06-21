from __future__ import unicode_literals
# lines that add some bits from other files

from django.conf import settings
from django.db import models
from django.utils import timezone
# we are defining object here
#post is the name of our model/class
#models.Model means that the Post is a django Model, so django knows that it should eb saved  in the databasr

class Post(models.Model): # this defines our model. it is an object
   #models.CharFIELD - this is how you define text with a limited number of characters
   #models.TextField - long text without a limit
   #models.DateTimeField - date and time
   #models.Foreignkey - this is a link to another model


    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length =200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


# publish method. publish is the name of the method
   #use lowercase and underscores insteadof spaces
    def publish(self):
        self.published_date = timezone.now()
        self.save()
#this method return string with a POst titlepy
    def __str__(self):
        return self.title