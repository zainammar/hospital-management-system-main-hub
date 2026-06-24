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


from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
from .models import Patient

def patient_pdf(request, id):
    patient = get_object_or_404(Patient, id=id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{patient.patient_id}.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100, 800, "Patient Report")
    p.drawString(300, 790, f"Date: {patient.date}")
    p.drawString(100, 780, f"Patient ID: {patient.patient_id}")
    p.drawString(300, 760, "Name:")
    p.drawString(300, 740, patient.patient_name)
    p.drawString(300, 780, f"Phone: {patient.phone}")
    p.drawString(100, 770, f"Prescription: {patient.prescription}")

# <p><b>Date:</b> {{ patient.date }}</p>

    p.showPage()
    p.save()

    return response