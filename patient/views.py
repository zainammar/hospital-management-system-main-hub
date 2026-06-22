from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

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

 # Edit

@login_required
def edit_patient(request, id):

    patient = Patient.objects.get(
        id=id,
        user=request.user
    )

    form = PatientForm(
        request.POST or None,
        instance=patient
    )

    if form.is_valid():
        form.save()
        return redirect('patient_list')

    return render(
        request,
        'patients/edit.html',
        {
            'form': form
        }
    )

def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

# Delete 


@login_required
def delete_patient(request, id):

    patient = Patient.objects.get(
        id=id,
        user=request.user
    )

    patient.delete()

    return redirect('patient_list')