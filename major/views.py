from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.db import  IntegrityError
from django.contrib.auth import login , logout , authenticate
from .form import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'major/home.html')

# Create your views here.
@login_required
def current(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'major/currentpage.html', {'todos': todos})


@login_required
def todoid(request,todoid_pk):
    todo = get_object_or_404(Todo, pk=todoid_pk, user=request.user)

    if request.method == 'GET':


        form = Todoform(instance=todo)
        return render(request, 'major/todoid.html', {'todo': todo, 'form': form})
    else:
        form = Todoform(request.POST,instance=todo)
        form.save()
        return redirect('current')




def signupuser(request):
    if request.method == 'GET' :
        return render(request , 'major/signupuser.html', {'form':UserCreationForm()})
    else :
        if request.POST['password2'] == request.POST['password1']:
            try:
                user  = User.objects.create_user(request.POST['username'] , password = request.POST['password1']  )
                user.save()
                login(request, user)
                return render(request, 'major/home.html')

            except IntegrityError :
                return render(request, 'major/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'user found !!'})

            return render(request, 'major/signupuser.html', {'form': UserCreationForm()})

        else:
            return render(request, 'major/signupuser.html', {'form': UserCreationForm() , 'error':'password did not match' })

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'major/loginuser.html', {'form': AuthenticationForm()})
    else:
        user=  authenticate(request , username=request.POST['username'] , password = request.POST['password'])
        if user is None:
            return render(request, 'major/loginuser.html', {'error': AuthenticationForm(),'error':'wrong !'} )
        else:
            login(request, user)
            return redirect('current')

@login_required
def logoutuser(request):
    if request.method=="POST":
       logout(request)
       return  redirect('homepage')


@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'major/createtodo.html', {'form': Todoform()})
    else:
        form = Todoform(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('current')



@login_required
def completed(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request, 'major/completedtodos.html', {'todos': todos})


@login_required
def complete(request,todoid_pk):
    todo = get_object_or_404(Todo, pk=todoid_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('current')
@login_required
def delete(request,todoid_pk):
    todo = get_object_or_404(Todo, pk=todoid_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('current')