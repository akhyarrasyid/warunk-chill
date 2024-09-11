from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'app_name': 'warunk_chill',
        'name': 'Akhyar Rasyid Asy syifa',
        'class_name': 'PBP - D'
    }
    return render(request, 'main.html', context)
