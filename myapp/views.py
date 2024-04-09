from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CandidateRegistrationForm,OrgRegisterForm,OrgLoginForm
from .models import Candidates
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "myapp/home.html")

def candidate_register(request):
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            candidate = form.save()
            resume_file = request.FILES.get('resume')
            if resume_file:
                candidate.resume = resume_file
            candidate.save()

            # Generate PDF resume
            pdf_content = generate_pdf(candidate)
            # Return PDF as response
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{candidate.name}-resume.pdf"'
            return response
    else:
        form = CandidateRegistrationForm()
    return render(request, 'myapp/candidateregister.html', {'form': form})
    # return render(request,"myapp/candidateregister.html")
def generate_pdf(candidate):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(220, 760, "{} Resume".format(candidate.name))
    # Personal Details Section (x,y)
    pdf.setFont("Helvetica", 12)

    pdf.drawString(100, 700, "Personal Details:")
    pdf.drawString(200, 700, "Name: {}".format(candidate.name))
    pdf.drawString(200, 680, "Email: {}".format(candidate.email))
    pdf.drawString(200, 660, "Phone Number: {}".format(candidate.phone_number))
    pdf.drawString(200, 640, "City: {}".format(candidate.city))
    pdf.drawString(200, 620, "Address: {}".format(candidate.address))
    # Education Details Section 80
    pdf.drawString(100, 540, "Education Details:")
    pdf.drawString(200, 540, "10th School: {}".format(candidate.tenth_school))
    pdf.drawString(200, 520, "10th Year: {}".format(candidate.tenth_year))
    pdf.drawString(200, 500, "10th Marks: {}".format(candidate.tenth_marks))
    pdf.drawString(200, 480, "12th School: {}".format(candidate.twelfth_school))
    pdf.drawString(200, 460, "12th Year: {}".format(candidate.twelfth_year))
    pdf.drawString(200, 440, "12th Marks: {}".format(candidate.twelfth_marks))
    # Technical Skills Section
    pdf.drawString(100, 360, "Technical Skills:")
    pdf.drawString(200, 360, "Skill 1: {}".format(candidate.skill1))
    pdf.drawString(200, 340, "Skill 2: {}".format(candidate.skill2))
    pdf.drawString(200, 320, "Skill 3: {}".format(candidate.skill3))
    # Interested Position Section
    interested_position = dict(candidate._meta.get_field('interested_position').choices)[candidate.interested_position]
    pdf.drawString(100, 240, "Interested Position: {}".format(interested_position))
    pdf.save()
    pdf_content = buffer.getvalue()
    buffer.close()
    return pdf_content

def organization(request):
    return render(request,"myapp/org.html")

def organization_signup(request):
    return render(request,"myapp/orgsignup.html")

def organization_signin(request):
    return render(request,"myapp/orgsignin.html")