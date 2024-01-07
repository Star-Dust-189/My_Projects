from django.db import models
import uuid
from django.contrib.auth.models import User

class Photographers(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Photographer' , default='')
    mobile = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    def __str__(self):
        return self.name

class Photographer_works(models.Model):
    photographer = models.OneToOneField(Photographers, on_delete=models.CASCADE)
    work_images = models.ImageField(upload_to='Photographer_work')

class Mehndi_Artist(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=50)
    Artist_image = models.ImageField(upload_to='MehndiArtist')
    mobile = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    def __str__(self):
        return self.name

class Mackup_Artist(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=50)
    Artist_image = models.ImageField(upload_to='MackupArtist')
    mobile = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    def __str__(self):
        return self.name

class Venue_Type(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    venue_type = models.CharField(max_length=50)

    def __str__(self):
        return self.venue_type

class Venue_Provider(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    venue_name = models.CharField(max_length=50)
    venue_image = models.ImageField(upload_to='VenueImage')
    mobile = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    veg_price = models.IntegerField()
    nonveg_price = models.IntegerField() 
    room_availability = models.IntegerField()

    Venue_Type = models.ForeignKey(Venue_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.venue_name

class Food_Categories(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Food_Categories = models.CharField(max_length=50)

    def __str__(self):
        return self.Food_Categories

class Food_Suplier(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=50)
    food_image = models.ImageField(upload_to='VenueImage')
    mobile = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()

    Food_Categories = models.ForeignKey(Food_Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




