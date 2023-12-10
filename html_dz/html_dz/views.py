from django.http import HttpResponse
from django.shortcuts import render

def reed(request):
    return HttpResponse('Это сработал reed')

def import_write(request):
    return render(request, 'import.html', {'greeting': 'user_text'})


def return_text(request):
    user_text = request.GET['usertext']
    return render(request, 'return.html', {'greeting': user_text})

# def tabl(request):
#     user_text = request.GET['usertext']
#     revers_text = user_text[::-1]
#     return render(request, 'test_html.html',{'usertext': user_text,'kkk': revers_text})

