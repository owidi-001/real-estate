import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from landlord.models import Landlord

from realestate.agent.models import Agent


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255, help_text="Eg kitchen, living etc")
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)


class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class HouseCategory(models.Model):
    # Reference: https://www.homestratosphere.com/types-of-houses/
    CATEGORIES = (
        ("apartment", "Apartment"),
        ("bungalow", "Bungalow"),
        ("airbnb", "AirBNB"),
        ("condominium", "Condominium"),
        ("cottage", "Cottage"),
        ("cabin", "Cabin"),
        ("container", "Container"),
        ("other", "Other")
    )
    category = models.CharField(max_length=100, choices=CATEGORIES)
    # icon = models.ImageField(upload_to="media")


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class House(models.Model):
    rent = models.FloatField(help_text="House rent in Ksh")
    bedrooms = models.IntegerField(help_text="Number of bedrooms")
    square_feet = models.FloatField(help_text="Description of house size in Square Feet")
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    STATUS = (
        ("V", "Vacant"),
        ("O", "Occupied"),
        ("B", "Booked")
    )
    status = models.CharField(max_length=1, choices=STATUS)
    units = models.IntegerField(default=1, help_text="Number of units available")
    STYLES = (
        ("contemporary", "Contemporary"),
        ("modern", "Modern"),
        ("flat", "Flats")
    )
    style = models.CharField()
    year_built = models.PositiveIntegerField(default=current_year(),
                                             validators=[MinValueValidator(1960), max_value_current_year])
    garage = models.IntegerField(default=0, help_text="How many garage does it have?")
    parking = models.IntegerField(default=0, help_text="How many cars can the house accommodate?")
    description = models.TextField(blank=True, null=True, help_text="Any other interesting fact to put out")
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)
    video_tour = models.SlugField(unique=True, blank=True, null=True, help_text="Video of room tour on youtube")
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)

# class Image(models.Model):
#     name = models.CharField(max_length=255, help_text="Eg kitchen, living etc")
#     house = models.ForeignKey(House, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')
#     default = models.BooleanField(default=False)
