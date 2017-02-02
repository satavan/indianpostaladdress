# Create your views here.
from django.shortcuts import render
from django.db import models
from .models import postindtable
from django.shortcuts import render_to_response
from .forms import PincodeForm
from django.template import Context

# Create your views here.
def import_db(request):
    
    f = open('/home/bhanu/Desktop/dj/newpostal/newindiapostal/csv/all_india_pin_code.csv', 'r')  
    for line in f:
        line =  line.split(',')
        tmp = postindtable.objects.create()
        tmp.officename = line[0]
        tmp.pincode= line[1]
        tmp.officeType = line[2]
        tmp.Deliverystatus = line[3]
        tmp.divisionname = line[4]
        tmp.regionname = line[5]
        tmp.circlename = line[6]
        tmp.taluk = line[7]
        tmp.Districtname = line[8]
        tmp.statename = line[9]
    	tmp.save()

    f.close()

def home(request):
    return render(request,'newindiapostal/da.html')

def retrieve(request):
    #x = postindtable.objects.get(pincode='PINCODE')
    if request.method == 'POST':
       form = PincodeForm(request.POST)
       print(form)
       if form.is_valid():
          PINCODE = request.POST.get('PINCODE')
          print(PINCODE)
          x = postindtable.objects.filter(pincode=PINCODE)
          print(x)
    return render_to_response("newindiapostal/ll.html", {'x':x}, context_instance=Context(request))
