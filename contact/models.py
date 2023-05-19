from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), # picture (imagem)

# Depois 2
# owner (foreign key)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.id}. {self.name}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1200, blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.id}. {self.first_name} {self.last_name}'
