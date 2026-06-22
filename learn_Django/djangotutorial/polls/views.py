from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
# from .poll import get_Poll_list , get_Detail_Poll , delete_Poll
from .models import Poll
from .forms import PollForm

# Create your views here
def home(request):
    query = request.GET.get('q')
    information_list = Poll.objects.all()
    if query:
        information_list = [poll for poll in information_list if query.lower() in poll.title.lower()]
    return render(request, 'home.html', {'inf_list': information_list})

def detail_info(request,id):
    infor_list = Poll.objects.get(id=id)
    return render(request, 'detail.html', {'info': infor_list})

def Search_Poll(request):
    query = request.GET.get('q')
    page = request.GET.get('page',1)
    return JsonResponse(
        {
            'query' : query,
            'page' : page
        }
    )
def delete_info(request, id):
   if request.method == 'POST':
       Poll.objects.filter(id=id).delete()
   return redirect('home')

def create_info(request):

    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PollForm()
    
    return render(request, 'create.html', {'form' : form})
        