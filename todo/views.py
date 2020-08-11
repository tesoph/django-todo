from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
#All django view functions have to take a request as the argument because they're handling the request
#And then they always have to return some kind of http response
def say_hello(request):
    return HttpResponse("Hello Wotrld")
    #now need to connect this to the browser ->> bycreating URLS

def get_todo_list(request):
    results = Item.objects.all()
    #a dictionary, the key is items and the value is results. results is all of class Items from the models.py
    return render(request,"todo_list.html", {'items': results})

def create_an_item(request):
    if request.method=="POST":
        form = ItemForm(request.POST, request.FILES)#files is usually used to "make sure if there's any files or anything being uploaded"(?)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form=ItemForm()
        #new_item = Item()
        #new_item.name = request.POST.get("name")
        #new_item.done = "done" in request.POST
        #new_item.save()
        #return redirect(get_todo_list)
    return render(request, "item_form.html", {"form": form})

def edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {"form": form})

def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)