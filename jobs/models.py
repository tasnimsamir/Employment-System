from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


Exper_LVL = (
    ('Junior','Junior'),
    ('Mid','Mid'),
    ('Senior','Senior'),
)


# Create your models here.

# class location(models.Model):
#     loc = models.CharField(max_length=50)

#     def __str__(self):
#         return self.loc

#job model
class job(models.Model):  # table 
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column
    
    experience_level = models.CharField(max_length=15 , choices=Exper_LVL)
    # loc = models.OneToOneField(location,on_delete=models.CASCADE)
    Programming_language = models.CharField(max_length=100,default='python')
    published_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000,default='There is no Job description.')
    
    slug = models.SlugField(blank=True, null=True)

    #Override Save function
    def save(self,*args, **kwargs): 
        self.slug = slugify(self.title+str(self.owner)) #save this value automatically while clicking 'save' button
        super(job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


#applicants model
class applicant(models.Model):
    applied_job = models.ForeignKey(job, related_name='apply_job', on_delete=models.CASCADE)
    national_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    biography = models.TextField(max_length=1000)
    Created_at = models.DateTimeField(auto_now=True)
    experience_level = models.CharField(max_length=15 , choices=Exper_LVL)
    # loc = models.OneToOneField(location,on_delete=models.CASCADE)
    Programming_language = models.CharField(max_length=100,default='python')
    

    def __str__(self):
        return self.name