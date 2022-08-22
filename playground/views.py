from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

def index(request):
    datas = Item.objects.all()
    inputForm = ItemForm()

    if request.method == "POST":
        formData = ItemForm(request.POST)
        if formData.is_valid():
            formData.save();
            return redirect("/")
    return render(request, "index.html", {"datas": datas, "form": inputForm})


def update(request, pk):
    updateData = Item.objects.get(id = pk)
    formData = ItemForm(instance = updateData)

    if request.method == "POST":
        myForm = ItemForm(request.POST, instance = updateData)
        if myForm.is_valid():
            myForm.save()
            return redirect("/")
    return render(request, "update.html", {"form": formData})

def delete(request, pk):
    getData = Item.objects.get(id = pk)

    if request.method == "POST":
        getData.delete()
        return redirect("/")
    return render(request, "delete.html", {"data": getData})

# Create your views here.
