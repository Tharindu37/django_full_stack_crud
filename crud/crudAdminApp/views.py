from django.shortcuts import render
from . models import postTable

# Create your views here.
def posts(request):
    # database = postTable.objects.all()
    # return render(request, 'index.html', {'database':database})
    database = postTable.objects.all()
    return render(request, 'index.html',{'database':database})


def post(request, pid):
    return render(request, 'post.html')