#imports;
#(after creating the Account & Transaction forms, they were added to this list).
from django.shortcuts import render, redirect #redirect was also added to this import.
from .forms import AccountForm, TransactionForm

#created functions to render the templates that we supplied via TTA;
def home(request):
    return render(request, 'checkbook/index.html')

def create_account(request):
    #the data below was inserted after adding the Account & Transaction forms in Imports(above).
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content) #content added.

def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')

def transaction(request):
    # the data below was inserted after adding the Account & Transaction forms in Imports(above).
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content) #content added.
