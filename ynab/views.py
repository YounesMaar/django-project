from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CustomerUserCreationForm,Depense, Budget,DepenseForm, BudgetForm
from django.contrib.auth import login,authenticate,logout,get_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def inscription(request):
   if request.method =="POST":
       form = CustomerUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('connexion')

   else:
        form =CustomerUserCreationForm( )
   return render(request,'inscription.html',{'form' :form})  

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, user.get_username())
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

@login_required
def acceuil(request):

    # 
    username = get_user(request).get_username()
    # passing the parameters to the context
    
    context = {
        'username': username,
    }
    
    return render(request,'acceuil.html', context)

def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def index(request):
    
    depenses = Depense.objects.filter(user=request.user)
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'ynab/index.html', {'depenses': depenses, 'budgets': budgets})

@login_required
def add_depense(request):
    
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = DepenseForm()
    return render(request, 'add_depense.html', {'form': form})

@login_required
def historique_depenses(request):
    
    depenses = Budget.objects.all()
    
    return render(request, 'depenses.html', {'depenses': depenses})

@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('index')
    else:
        form = BudgetForm()
    return render(request, 'add_budget.html', {'form': form})


@login_required
def historique_budgets(request):
    
    budgets = Budget.objects.all()
    
    return render(request, 'budgets.html', {'budgets': budgets})
