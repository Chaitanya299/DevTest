import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            # Detect if it's Excel or CSV
            if file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            elif file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                return HttpResponse('File format not supported.')

            summary = df.groupby(['Cust State', 'Cust Pin']).agg({'DPD': 'sum'}).reset_index()
            return render(request, 'filehandler/report.html', {'summary': summary})

    else:
        form = UploadFileForm()

    return render(request, 'filehandler/upload.html', {'form': form})