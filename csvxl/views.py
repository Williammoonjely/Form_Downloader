from os import rename
from django.shortcuts import redirect, render
from .forms import InfoForm
import csv
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    infoform = InfoForm()
    
    if request.method == 'POST':
        dataform = InfoForm(request.POST)
        if dataform.is_valid():
            cd = dataform.cleaned_data
            fname = cd['first_name']                     
            lname = cd['last_name']
            adhaar = cd['adhaar_number']
            account = cd['account_number']
            print(fname,lname,adhaar,account)
            
            response = HttpResponse(content_type='text/csv')  
            response['Content-Disposition'] = 'attachment; filename="file.txt"'  
            writer = csv.writer(response)    
            writer.writerow([f'{fname}#~#{lname}#~#{adhaar}#~#{account}'])
            resp = response  
            return resp
            # need to add how to go to a new form page automaticaly
      
    return render(request,'form.html',{ 'infoform' : infoform})