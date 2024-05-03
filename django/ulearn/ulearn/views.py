from django.shortcuts import render, redirect
from ulearn.models import Person
from ulearn.forms import AddPersonForm



def index_page(request):
    persons = Person.objects.all()
    s = ""
    for person in persons:
        s += f"<h3>{person}: возраст - {person.age}, должность - {person.job}</h3>"
    return render(request, "index.html", context={"person_list": s})


def add_page(request):
    form = AddPersonForm()
    return render(request, "add.html", context={"form": form})


def add_person(request):
    form = AddPersonForm(request.POST)

    if form.is_valid():
        try:
            Person.objects.create(
                first_name=form.cleaned_data['fname'], 
                last_name=form.cleaned_data['lname'], 
                age=form.cleaned_data['age'], 
                job=form.cleaned_data['job']
            )
        except:
            print("[ERROR]: Form was not filled correctly")

    return redirect(index_page)
