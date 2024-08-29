import requests
from django.shortcuts import render, get_object_or_404, redirect
import wikipediaapi
from .models import WikiPage
from .forms import wikiPageForm

# Create your views here.
def view_page(request, title):
    page = get_object_or_404(WikiPage, title=title)
    return render(request, 'wiki/view_page.html', {'page': page})

def create_page(request):
    if request.method == 'POST':
        form = wikiPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_page', title=form.cleaned_data['title'])
    else:
        form = wikiPageForm()
    return render(request, 'wiki/create_page.html', {'form': form})

def search_pages(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Prepare the Wikipedia API request
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'search',
            'srsearch': query,
            'utf8': 1
        }

        # Make the API request
        response = requests.get(url, params=params, headers={'User-Agent': 'Wikipedia Clone/1.0 (https://yourwebsite.com/; your-email@example.com)'})
        data = response.json()

        # Process the search results
        if 'query' in data and 'search' in data['query']:
            for item in data['query']['search']:
                title = item['title']
                snippet = item['snippet']  # Summary of the content
                pageid = item['pageid']
                fullurl = f"https://en.wikipedia.org/?curid={pageid}"

                results.append({
                    'title': title,
                    'summary': snippet,
                    'url': fullurl
                })

    return render(request, 'wiki/search_results.html', {'query': query, 'results': results})

