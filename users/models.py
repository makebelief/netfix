from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user model for Netfix application."""
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username
    


class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    field = models.CharField(max_length=70, choices=(('Air Conditioner', 'Air Conditioner'),
                                                     ('All in One', 'All in One'),
                                                     ('Carpentry', 'Carpentry'),
                                                     ('Electricity',
                                                      'Electricity'),
                                                     ('Gardening', 'Gardening'),
                                                     ('Home Machines',
                                                      'Home Machines'),
                                                     ('House Keeping',
                                                      'House Keeping'),
                                                     ('Interior Design',
                                                      'Interior Design'),
                                                     ('Locks', 'Locks'),
                                                     ('Painting', 'Painting'),
                                                     ('Plumbing', 'Plumbing'),
                                                     ('Water Heaters', 'Water Heaters')), blank=False, null=False)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)

    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username
