# credit/views.py
from django.shortcuts import render, get_object_or_404
from .models import Report

def credit_home(request):
    return render(request, 'credit/credit_home.html')

def report(request):
    reports = Report.objects.all()
    return render(request, 'credit/report.html', {'reports': reports})

def report_detail(request, id):
    report = get_object_or_404(Report, id=id)
    return render(request, 'credit/report_detail.html', {'report': report})

def charge(request):
    if request.method == 'POST':
     
        return render(request, 'credit/charge_success.html')
    return render(request, 'credit/charge.html')
