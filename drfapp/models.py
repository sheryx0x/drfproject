from django.db import models

class snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100 , blank=True , default='')
    code = models.TextField()
    language = models.CharField(max_length=100 , default='python')
    style = models.CharField(default='friendly' , max_length=100)
    
    class Meta:
        ordering  = ['created']