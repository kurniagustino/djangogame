from django.shortcuts import render

def list(request):
    context = {
        'title':'Tammu Game News'
    }
    return render(request, 'index.html', context)