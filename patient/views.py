from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Patient
from .forms import PatientForm


@login_required
def patient_list(request):

    patients = Patient.objects.filter(user=request.user)

    return render(
        request,
        'patients/list.html',
        {
            'patients': patients
        }
    )


@login_required
def add_patient(request):

    form = PatientForm(request.POST or None)

    if request.method == "POST":
        print(form.errors)

    if form.is_valid():

        patient = form.save(commit=False)
        patient.user = request.user
        patient.save()

        print("PATIENT SAVED")

        return redirect('patient_list')

    return render(
        request,
        'patients/add.html',
        {
            'form': form
        }
    )