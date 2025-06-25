from django.shortcuts import render, HttpResponse, redirect
from .models import *

from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from PIL import Image as PilImage
from django.core.files.base import ContentFile
import io
import os


# Create your views here.
def index(request):

    return render(request, "index.html", {
        "services": Service.objects.all(),
        "images": Image.objects.all()[:5],
    })

def about(request):
    return render(request, 'about.html',)

def thanks(request):
    return render(request, 'thanks.html',)
def realizations(request):
    return render(request, 'realizations.html', {
        'categories': Category.objects.all()
    })
@login_required(login_url='/admin/core')
def upload(request):
    if request.method == "POST":
        files = request.FILES.getlist('images[]')
        print(files)
        for file in files:
            img_obj = Image.objects.create(
                category=Category.objects.get(id=request.POST["category"]),
                images=file
            )
            pil_img = PilImage.open(img_obj.images.path)
            pil_img = pil_img.convert("RGB")
            if pil_img.width > 1280:
                ratio = 1280 / float(pil_img.width)
                height = int(float(pil_img.height) * ratio)
                pil_img = pil_img.resize((1280, height), PilImage.Resampling.LANCZOS)
            buffer = io.BytesIO()
            pil_img.save(buffer, format="WEBP")
            filename = os.path.splitext(file.name)[0] + ".webp"
            img_obj.optimized.save(filename, ContentFile(buffer.getvalue()), save=True)
        return redirect('realizations')
    return render(request, 'create.html', {
        'category': Category.objects.all()
    })

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        print(request.FILES)
        print(form.is_valid())
        if form.is_valid():
            customer = Customer.objects.create(
                fname=form.cleaned_data['fname'],
                lname=form.cleaned_data['lname'],
                address=form.cleaned_data['address'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                category=form.cleaned_data['category'],
                details=form.cleaned_data['details']
            )
            # 1. Email firme (kópia správy)
            email = EmailMessage(
                subject=f'Nová správa z kontaktného formulára od {customer.fname} {customer.lname}',
                body=f"{customer.details}\n {customer.email}\n {customer.phone}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['lfstrechy@gmail.com'],
            )
            for f in request.FILES.getlist('attachment'):
                email.attach(f.name, f.read(), f.content_type)
            email.send(fail_silently=False)

            # 2. Potvrdenie uchádzačovi
            confirm_message = (
                f"Dobrý deň {customer.fname} {customer.lname},\n\n"
                "ďakujeme za vašu správu. Bola úspešne zaevidovaná.\n"
                "Budeme vás čo najskôr kontaktovať.\n\n"
                "S pozdravom,\n Lukáš Vaško \n +421 948 337 362\n lfstrechy@gmail.com"
            )
            send_mail(
                subject='Vaša správa bola prijatá',
                message=confirm_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer.email],
                fail_silently=False,
            )

            # 3. Presmerovanie na ďakovnú stránku
            return render(request, 'thanks.html')

        else:
            print(form.errors)
            return render(request, 'fail.html')
        

    else:

        serviceid = request.GET.get('serviceid')

        if serviceid is not None:
            try:
                serviceid = int(serviceid)
            except ValueError:
                return HttpResponse("Hodnota nie je číslo.")

        return render(request, 'contact.html', {
            'select': serviceid,
            'services': Service.objects.all(),
        })