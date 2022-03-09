from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Customer,transactionhistory
from django.db.models import F
from datetime import datetime
# Create your views here.
def home(request):
    return render(request ,'home.html')
def help(request):
    return render(request,'help.html')

def customer(request):
    cus = Customer.objects.all()
    return render(request , 'customer.html',{'cus':cus})

def transfer(request):
    if request.method=='POST':
        cust = request.POST.get('submit')
        query1 = Customer.objects.get(name=cust)
        query2 = Customer.objects.exclude(name=cust)
        context = {
        'cust_name' : query1,
        'all_details' : query2
        }
        return render(request,'transfer.html',context)
    if request.method=='GET':
        return render(request,'transfer.html')
def transactions(request):
    if request.method =="POST":
        receiver= request.POST.get('to')
        money = request.POST.get('amount')

        sender = request.POST.get('submit')
        query2 = Customer.objects.get(name = sender)
        query2.balance= F('balance')- money
        query2.save()
        query1 = Customer.objects.get(name= receiver)
        query1.balance= F('balance')+ money
        query1.save()
        result = Customer.objects.get(name = sender)
        transact = transactionhistory()
        transact.source_name = sender
        transact.source_email = result.email
        transact.available_balance = result.balance
        transact.transfered_amount = money
        transact.source_accountnumber = result.accountnumber
        transact.destination_name = receiver
        transact.date = datetime.today()
        transact.save()
        return redirect('transactions')
    all_entries = transactionhistory.objects.all()
    context = {
        "history" : all_entries
        }
    return render(request, 'transactions.html', context)
