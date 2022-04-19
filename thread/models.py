from django.db import models 



class Topic(models.Model):
    user = models.CharField(max_length=50, blank=False, null=True)
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title


    


class Comment(models.Model):
    name = models.CharField('名前', max_length=200, default='名無しのycu')
    text = models.TextField('')
    target = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='対象スレッド')
    created_at = models.DateTimeField('日時', auto_now_add=True)
    
    def __str__(self):
        return self.text[:20]
    
    