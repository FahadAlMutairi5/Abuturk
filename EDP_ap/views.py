from django.shortcuts import render
from .models import InformationModel 
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import datetime


# Create your views here.
def home(request):
    informationModel = InformationModel.objects.get(id=1)

    works_com = informationModel.works_com
    years_of_ex = informationModel.years_of_ex
    total_clients = informationModel.total_clients

    now = datetime.datetime.now()

    context = {
        "year" : now.year,
        "years_of_ex": years_of_ex,
        "total_clients": total_clients,
        "works_com"  : works_com,
    }
    return render(request, 'home.html', context)


def detail_p(request, prot_id):
    prot = ProtModel.objects.get(id=prot_id)
    context = {
        "protf": prot,
    }
    return render(request, 'service_detail.html', context)


def about_us(request):
    return render(request, 'about_us.html')

def send_email_fun(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    mssg = """
        """+message+"""

        """+from_email+"""
    """
    print (from_email)
    if subject and message and from_email:
        try:
            send_mail(subject+name, mssg, from_email, ['devsof5e@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    
