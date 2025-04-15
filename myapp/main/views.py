from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def home(response):
    return render(response, "main/home.html",{})

#custom form
def getls(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)

        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            res = response.POST.get("new")
            if res and len(res) > 5:
                ls.item_set.create(text=res, complete=False)
            else:
                print("not a proper task")

    return render(response, "main/list_item.html", {"ls": ls})

#django form in .forms.py
# def create(response):
#     if response.method == "POST":
#         form = CreateNewList(response.POST)
#         if form.is_valid():
#             n = form.cleaned_data["name"]
#             response.user.todolist_set.create("name":n)
#         return HttpResponseRedirect("/%i"%t.id)
#     else:
#         form = CreateNewList()
#     return render(response, "main/create_list.html",{"form":form})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = response.user.todolist_set.create(name=n)
            return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create_list.html", {"form": form})

def view(response):
    ls = ToDoList.objects.all()
    return render(response, "main/view_lists.html", {"ls": ls})
