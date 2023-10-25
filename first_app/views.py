from django.shortcuts import render, redirect
# from django.http import HttpResponse 
from .forms import CourseForm
from django.urls import reverse
from .models import course
# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def first_year(request):
    pp = course.objects.filter(year=1)
    args={'pp':pp}
    return render(request, 'first_app/first_year.html', args)

def second_year(request):
    pp = course.objects.filter(year=2)
    return render(request, 'first_app/second_year.html', {'pp':pp})

def third_year(request):
    pp = course.objects.filter(year=3)
    return render(request, 'first_app/third_year.html', {'pp':pp})

def fourth_year(request):
    pp = course.objects.filter(year=4)
    return render(request, 'first_app/fourth_year.html', {'pp':pp})

def teach(request):
    if request.method == 'POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            toi = form.cleaned_data
            print(toi)
            if toi['year']==1:
                return redirect(reverse('first_app:first_year'))
            elif toi['year']==2:
                return redirect(reverse('first_app:second_year'))
            elif toi['year']==3:
                return redirect(reverse('first_app:third_year'))
            elif toi['year']==4:
                return redirect(reverse('first_app:fourth_year'))
        else:
            print('form not valid')
    else:
        form=CourseForm()
        return render(request, 'first_app/teach.html', context={'form':form})

def about(request):
    return render(request, 'first_app/about.html')