from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from modelapp.models import crud

# Create your views here.


def index(request):
    data = crud.objects.all()
    # print(data.values())
    if request.method == "POST":
        password = request.POST.get("password")
        crud.objects.create(password=password) 
        return render(request, 'index.html' , {'data':data})

    return render(request, 'index.html',{'data':data})


def update(request, id):
    data = get_object_or_404(crud , id=id)
    if request.method=="POST":
        password = request.POST.get("password")
        data.password = password
        data.save()
        return redirect('/')
    return render(request, 'update.html',{'data':data})


def delete(request , id):
    data = get_object_or_404(crud , id=id)
    print(id)
    data.delete()
    return redirect('/')

