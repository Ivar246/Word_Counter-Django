from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'home.html')

def show_result(request):
    text = request.POST['textarea']
    length = len(text.split())
    
    return render(request, 'result.html', {
        'length': length
    })