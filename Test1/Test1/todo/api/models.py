from django.db import models


class List(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'list'
    
    def __str__(self):
        return self.title
    
    
