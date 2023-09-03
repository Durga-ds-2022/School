from django.db import models

# Create your models here.

class RegisterStudent(models.Model):
    student_name = models.CharField(max_length=100)
    parents_name = models.CharField(max_length=100)
    email= models.EmailField(blank= True, max_length=254)
    moblie= models.IntegerField( max_length= 10)

    def __str__(self):
        return self.student_name
    
    
class Testimonial(models.Model):
    parent_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message= models.CharField( max_length=500)
    photo= models.ImageField(upload_to="testimonial", height_field=None, width_field=None, max_length=None)
    is_display= models.BooleanField(default=False)

    def __str__(self):
        return self.parent_name
    
class Alumni(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message= models.CharField( max_length=500)
    photo= models.ImageField(upload_to="Alumni", height_field=None, width_field=None, max_length=None)
    is_display= models.BooleanField(default=False)

    def __str__(self):
        return self.student_name
    
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.CharField( max_length=500)
    photo= models.ImageField(upload_to="Event", height_field=None, width_field=None, max_length=None)
    video = models.FileField( upload_to="event_image/video_link", blank=True)
    is_display= models.BooleanField(default=False)
    is_video_display= models.BooleanField(default=False)

    def __str__(self):
        return self.event_name
    

class ImageCetegory(models.Model):
    category_name= models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class Gallery(models.Model):
    photo= models.ImageField(upload_to= "Gallery", height_field=None, width_field=None, max_length=None, blank=True, null=True)
    video = models.FileField( upload_to="Video/video_link", blank=True)
    category= models.ForeignKey(ImageCetegory, on_delete=models.CASCADE, related_name="category")
    is_display= models.BooleanField(default=False)
    is_home_page= models.BooleanField(default=False)

    def __str__(self):
        return self.category.category_name
     
    
class Career(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField( max_length=254, unique=True)
    address= models.TextField()
    city= models.CharField(max_length=100)    
    pincode= models.IntegerField()
    date= models.DateField(auto_now=True, auto_now_add=False)
    resume= models.FileField(upload_to='resume', max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Announcements(models.Model):
    news= models.CharField(max_length=500, default="Na")
    is_display= models.BooleanField(default=False)

    def __str__(self):
        return self.news[:100]

class Feedback(models.Model):
    name= models.CharField(max_length=500)
    subject= models.CharField(max_length=500)
    email= models.EmailField( max_length=254)
    message= models.TextField()

    