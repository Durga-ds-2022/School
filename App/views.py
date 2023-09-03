from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from .models import *
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method== "POST":
        student_name = request.POST.get("student_name")
        parents_name = request.POST.get('parents_name')
        email = request.POST.get('email')
        moblie = request.POST.get('moblie')
        
        res_obj= RegisterStudent.objects.create(
            student_name=student_name,
            parents_name= parents_name,
            email= email,
            moblie = moblie
        )
        return redirect('home')
    home_image = Gallery.objects.filter(is_home_page=True, is_display=True)
    announcements = Announcements.objects.filter(is_display= True)[:10]
    home_event= Event.objects.filter(is_display= True)[:3]
    testimonial= Testimonial.objects.filter(is_display= True)[:3]
    alumni= Alumni.objects.filter(is_display= True)[:3]
    context=  {'home_image': home_image,
                'home_event': home_event,
                'testimonial': testimonial,
                'alumni': alumni,
                'announcements': announcements
                }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def facilities(request):
    return render(request, "facilities.html")

def testimonial(request):
    if request.method== "POST":
            parent_name = request.POST.get("parent_name")
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            test_obj= Testimonial.objects.create(
                parent_name= parent_name,
                email= email,
                message = message,
                is_display= True
            )
            return redirect('home')
    testimonial= Testimonial.objects.filter(is_display= True)[:4]
    alumni= Alumni.objects.filter(is_display= True)[:4]

    return render(request, "testimonial.html", {'testimonials': testimonial,'alumni': alumni, })

def events(request):
    event_obj= Event.objects.all()
    paginator = Paginator(event_obj, 6)  # Show 12 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'event_obj': page_obj,  # Use page_obj here instead of event_obj
    }
    return render(request, "events.html", context)

def careers(request):
    return render(request, "careers.html")

def contact(request):
    if request.method== "POST":
            name = request.POST.get("name")
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            
            test_obj= Feedback.objects.create(
                name= name,
                email= email,
                message = message,
                subject= subject,
            )
            return redirect('home')
    return render(request, "contact.html")

def gallery(request):
    categories = ImageCetegory.objects.values('category_name')
    category_filter = request.GET.get('category')
    if category_filter:
        g_obj = Gallery.objects.filter(is_display=True, category__category_name=category_filter, is_home_page=False)
    else:
        g_obj = Gallery.objects.filter(is_display=True, is_home_page=False)

    paginator = Paginator(g_obj, 12)  # Show 12 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'g_obj': page_obj,  # Use page_obj here instead of g_obj
        'category_filter': category_filter
    }
    return render(request, "gallery.html", context)

def resgistration(request):
    if request.method== "POST":
        student_name = request.POST.get("student_name")
        parents_name = request.POST.get('parents_name')
        email = request.POST.get('email')
        moblie = request.POST.get('moblie')
        
        res_obj= RegisterStudent.objects.create(
            student_name=student_name,
            parents_name= parents_name,
            email= email,
            moblie = moblie
        )
        return redirect('home')
       
    return render(request, "registration.html")


def event_details(request):
    return render(request, 'event-details.html')