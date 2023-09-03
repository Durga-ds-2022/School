from .views import *
from django.urls import path
urlpatterns = [
    path("", index, name= "home"),
    path("about-us/", about, name= "about"),
    path("facilities/", facilities, name= "facilities"),
    path("testimonial/", testimonial, name= "testimonial"),
    path("events/", events, name= "events"),
    path("careers/", careers, name= "careers"),
    path("contact/", contact, name= "contact"),
    path("gallery/", gallery, name= "gallery"),
    path("registration/", resgistration, name= "registration"),
    path("event-details/", event_details, name= "event_details"),

    
]