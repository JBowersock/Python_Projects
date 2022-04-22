#imports;
#(after creating the Account & Transaction forms, they were added to this list).
from django.shortcuts import render, redirect, get_object_or_404 #pay attention to these additions.
from .models import Account, Transaction #this one was added later.
from .forms import AccountForm, TransactionForm

#created functions to render the templates that we supplied via TTA;
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == "POST":
        pk = request.POST['account']
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content) #content added.

def create_account(request):
    #the data below was inserted after adding the Account & Transaction forms in Imports(above).
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content) #content added.

def balance(request, pk): #primary key
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transactions.filter(account = pk)
    current_total = account.initial_deposit
    table_contents = { }
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content) #content added.

def transaction(request):
    # the data below was inserted after adding the Account & Transaction forms in Imports(above).
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #the following 3 lines were altered at a later time.
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content) #content added.
