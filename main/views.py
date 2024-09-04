from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207165',
        'name': 'Felita Zahra Diyanti',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)