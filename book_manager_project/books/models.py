from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100);
    author = models.CharField(max_length=200);
    publication_date = models.DateField();
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True);
    
    def __str__(self):
        return self.title
    
