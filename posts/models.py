""" models posts """
# Create your models here.
# my database will be here

# users models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Problem(models.Model):
    """ profile model 
    Proxy model that extends the base data with  other
    information
    """
    pass