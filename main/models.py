from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=55)
    date_of_found = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='brands')

    def __str__(self):
        return f'{self.name}'


class Model(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name


class Watch(models.Model):

    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')

    )
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='watches')
    status = models.CharField(choices=CHOICES, max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='watches')
    model = models.ManyToManyField(Model)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('home')




