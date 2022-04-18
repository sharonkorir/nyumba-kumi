from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Business
from .forms import CreateNeighbourhoodForm

# Create your views here.
@login_required()
def index(request):
  return render(request,'index.html')

def search_results(request):
    '''
    Function to search for businesses
    
    Args: search term
    '''

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def create_neighbourhood(request):
    if request.method == 'POST':
        form = CreateNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user.profile.pk
            neighbourhood.save()
            return redirect('neighbourhood')
    else:
        form = CreateNeighbourhoodForm()
    return render(request, 'neighbourhoods/create_neighbourhood.html', {'form':form})
        