from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
# Create your models here.


class Adress(models.Model):
    street = models.CharField(max_length = 80)
    postal_code = models.CharField(max_length = 5)
    city = models.CharField(max_length = 50)
    
    def __str__(self):
        return f"{self.street},{self.postal_code},{self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"
        
class Country(models.Model):
    name=models.CharField(max_length=80)
    code=models.CharField(max_length=2)
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    adress=models.OneToOneField(Adress, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length = 50)
    rating = models.IntegerField()
    author =models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False,db_index = True,blank=True)
    published_countries= models.ManyToManyField(Country)
    
    
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])
    
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args,**kwargs)
    
    
    def __str__(self):
        return f"{self.title} ({self.rating})"