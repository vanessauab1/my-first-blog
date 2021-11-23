from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField, forms
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # fotoCapa = models.ImageField() - versão 1
    # fotoCapa = models.ResizedImageField() - versão 2
    fotoCapa =ResizedImageField(size=[400, 300], upload_to='media/', blank=True, null=True, force_format = 'png' )
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    campoURL1  = models.URLField('URL',null=True,blank=True) 
    campoURL2  = models.URLField('URL',null=True,blank=True) 
    campoURL3  = models.URLField('URL',null=True,blank=True)      

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
