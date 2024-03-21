from django.db import models
from django.contrib.postgres.fields import RangeField
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Service(BaseModel):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Type(BaseModel):
    name = models.CharField(max_length=50)


class Establishment(BaseModel):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price_for_entrance = RangeField(models.IntegerField())
    capacity = models.IntegerField()
    services = models.ManyToManyField(Service, related_name='establishments')
    address = models.CharField(max_length=40)
    additional_services = models.ManyToManyField(Service)
    work_mobile_number = models.CharField(max_length=15)
    recommended = models.BooleanField(default=False)
    rating = models.FloatField()

    def __str__(self): 
        return f"{self.name}({self.type})"


class Comment(BaseModel):
    author = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField(500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.author}({self.created_at})"
