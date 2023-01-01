from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
JOB_TYPE=(
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
)


def image_upload(instance,filename):
    imagename ,extension = filename.split('.')
    return "jobs/%s.%s"% (instance.id,extension)

class Job(models.Model):
    owner  = models.ForeignKey(User,related_name='job_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    job_type = models.CharField(default="" ,max_length = 20 , choices=JOB_TYPE)
    description = models.TextField(max_length=500,null=True)
    published_at =  models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary  = models.IntegerField(default= 0 )
    experience  = models.IntegerField(default= 1 )
    category = models.ForeignKey('Category', on_delete =models.CASCADE ,default =False)
    image = models.ImageField(upload_to = image_upload) 
    slug = models.SlugField(null=True, blank=True)  
    class Meta:
        verbose_name_plural = 'Jobs'
    
    def save(self,*args,**kwargs):
        self.slug =slugify(self.title)
        super(Job,self).save( *args ,**kwargs)


    def __str__(self):
        return self.title  

class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Categories'
    


    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job' ,on_delete=models.CASCADE)  
    #owner  = models.ForeignKey(User,related_name='job_author' ,on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=150)
    website = models.URLField(null = True,blank =True)
    cv=models.FileField(upload_to='apply/')        
    cover_letter = models.TextField(max_length=600)
    cerated_at =  models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Applies'
    def __str__(self):
        return self.name


