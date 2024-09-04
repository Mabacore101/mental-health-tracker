from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306206446',
        'name': 'Valentino Vieri Zhuo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
