from django.db import models

# Model is a parent class included in Django that defines a model's basic functionality
# 0. Add the project to the INSTALLED_APPS = [ ... 'my_app']
# 1. py manage.py makemigrations learning_logs 
# 2. py manage.py migrate 
 
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text 

