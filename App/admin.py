from django.contrib import admin

# Register your models here.
from .models import (RegisterStudent, 
Testimonial, 
Alumni, 
Event, 
ImageCetegory, 
Gallery, 
Career, 
Announcements, Feedback )

admin.site.register(RegisterStudent)
admin.site.register(Testimonial)
admin.site.register(Alumni)
admin.site.register(ImageCetegory)
admin.site.register(Gallery)
admin.site.register(Career)
admin.site.register(Announcements)
admin.site.register(Event)
admin.site.register(Feedback)
