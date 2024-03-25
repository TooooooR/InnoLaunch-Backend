from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import IntegerRangeField


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Address(BaseModel):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    build_number = models.CharField(max_length=10)

    def str(self):
        return f'{self.city}, {self.street}, {self.build_number}'


class Photo(BaseModel):
    image = models.ImageField()


class Price(BaseModel):
    amount = IntegerRangeField(validators=[MinValueValidator(0)])
    payment_type = models.CharField(max_length=200)

    def str(self):
        return f'{self.amount} - {self.payment_type}'


class Establishment(BaseModel):
    slug = models.SlugField(max_length=80)
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=30)
    price = models.OneToOneField(Price, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    work_mobile_number = models.CharField(max_length=15)
    recommended = models.BooleanField(default=False)
    photos = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)
    rating = models.FloatField()

    def str(self):
        return f"{self.name} - {self.work_mobile_number}"


class Amenity(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    establishments = models.ManyToManyField(Establishment, related_name='amenities')

    def str(self):
        return f'{self.name}'


class Service(BaseModel):
    name = models.CharField(max_length=100)
    establishments = models.ManyToManyField(Establishment, related_name='services', blank=True)

    def str(self):
        return f'{self.name}'


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

    def str(self):
        return f"{self.author}({self.created_at})"
