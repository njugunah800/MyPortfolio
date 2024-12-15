
from django.shortcuts import render,redirect

from portfolioapp.forms import ContactForm
from portfolioapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter-page.html')

def contact(request):
    if request.method == "POST":
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/contactshow')
    else:
         return render(request,'contact.html')

def contactshow(request):
    allcontacts = Contact.objects.all()
    return render(request,'contactshow.html',{'allcontacts': allcontacts})

def deleteContact(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/contactshow')

def editContact(request,id):
    editcontact = Contact.objects.get(id=id)
    return render(request, 'editcontact.html',{'contact':editcontact})

def updateContact(request,id):
    updateinfo = Contact.objects.get(id=id)
    form = ContactForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/contactshow')
    else:
        return render (request,'editcontact.html')

def about(request):
    return render(request,'about.html')


def resume(request):
    return render(request,'resume.html')


def testimonials(request):
    return render(request,'testimonials.html')
