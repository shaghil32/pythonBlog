from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # add in author later

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:100]+"...."

'''
the below command is used to make a migration file to apply the migrations, by looking 
at the difference between two migrations files django get to know the new changes in 
the model then apply those changes in the db.

$python manage.py makemigrations 

The below command apply the migrations from the migration file made by above command
$python manage.py migrate
'''