from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from neighbourhood.models import Business

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