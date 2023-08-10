from django.shortcuts import render, redirect
from .models import Category, Week
from .forms import WeekForm  # Создайте форму для недели

from .templatetags.custom_filters import get_attribute


def index(request):
    categories = Category.objects.all()
    weeks = Week.objects.all()
    fields = [field for field in Week._meta.fields if field.name not in ['id', 'date']]

    context = {
        'categories': categories,
        'weeks': weeks,
        'fields': fields,

    }
    
    return render(request, 'index.html', context)




def add_week(request):
    if request.method == 'POST':
        form = WeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Замените на нужный URL
    else:
        form = WeekForm()

    return render(request, 'add-week.html', {'form': form})

