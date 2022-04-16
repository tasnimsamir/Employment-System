from jobs.models import applicant
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.



class Profile(models.Model):
    applicant = models.ForeignKey(applicant,related_name='applicant',on_delete=models.CASCADE,blank=True,null=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # location = models.OneToOneField(location, on_delete=models.CASCADE,default='Cairo')
    phone_number = models.CharField(max_length=15)
    company = models.CharField(max_length=100,default='Django_admin')


    def __str__(self):
        return str(self.user)

## create new user ---> create new empty profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


