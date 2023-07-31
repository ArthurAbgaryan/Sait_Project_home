from django.db import models




class Post(models.Model):
    title=models.CharField(max_length = 200, verbose_name = "Название статьи", db_index = True)
    content = models.TextField(max_length = 5000, verbose_name = "Контент", blank = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length = 50)
    like = models.ManyToManyField(User)
    coment = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
    
    def like_total(self):
        return like.count()
    
    def coment_total(self):
        return coment.count()
    
    

# Create your models here.
