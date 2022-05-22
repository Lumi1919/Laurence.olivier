from django.shortcuts import render, redirect
from .models import ReservationsSeance
from .formulaires import ReservationsSeanceForm


def index(request):
    return render(request, 'index.html')


def ReservationSeance(request):
    model = ReservationsSeance
    form_class = ReservationsSeanceForm
    if request.method == "POST":
        form = ReservationsSeanceForm(request.POST).save()
        return redirect('/confirmation')

    else:
        form = ReservationsSeanceForm()

    return render(request, 'about_us.html', {'form': form, 'dataReservations': ReservationsSeance.objects.all()})


def ContactPage(request):
    return render(request, 'contact_us.html')

def GalleryPage(request):
    return render(request, 'gallery.html')


def confirmationPage(request):
    return render(request, 'confirmation.html')


