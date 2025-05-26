from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):

    return render(request, "index.html", {
        "services": Service.objects.all(),
        "references": Realization.objects.all(),
    })

def about(request):
    return render(request, 'about.html',)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.create(
                fname=form.cleaned_data['fname'],
                lname=form.cleaned_data['lname'],
                adress=form.cleaned_data['adress'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                category=form.cleaned_data['category'],
                details=form.cleaned_data['details']
            )
            # tu môžeš napr. logovať zákazníkovu žiadosť o službu
            # alebo vytvoriť nový model Request(customer=..., service=..., details=...)
            print(f"{customer.fname} si vyžiadal službu {form.cleaned_data['category'].title}")
            return HttpResponse(f"{customer.fname} si vyžiadal službu {form.cleaned_data['category'].title}")
        else:
            print("chyba")
            return HttpResponse("chyba")
    else:
        form = ContactForm()

        serviceid = request.GET.get('serviceid')

        if serviceid is not None:
            try:
                serviceid = int(serviceid)
            except ValueError:
                return HttpResponse("Hodnota nie je číslo.")

        return render(request, 'contact.html', {
            'select': serviceid,
            'services': Service.objects.all(),
            "references": Realization.objects.all(),
        })