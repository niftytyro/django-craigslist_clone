from django.shortcuts import render
from . import models

import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup


CRAIGSLIST_BASE_URL = 'https://indore.craigslist.org/search/?query={}'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    try:
        url = CRAIGSLIST_BASE_URL.format(quote_plus(search))
        response = requests.get(url, allow_redirects=True)
        data = response.text

        soup = BeautifulSoup(data, 'html.parser')
        post_listings = soup.find_all('li', {'class': 'result-row'})

        final_post_listings = []
        for post in post_listings:
            post_title = post.find(class_='result-title').text
            post_url = post.find('a').get('href')
            post_price = post.find(class_='result-price')
            if(post_price):
                post_price = post_price.text
            else:
                post_price = 'N/A'
            image_soup = BeautifulSoup(requests.get(post_url).text, 'html.parser')
            post_image_url = image_soup.find('img')
            if(post_image_url):
                post_image_url = post_image_url.get('src')
            else:
                post_image_url = ''
            final_post_listings.append((post_title, post_url, post_price, post_image_url))
    except:
        final_post_listings = []

    data_for_frontend = {
        'search': search,
        'post_listings': final_post_listings,
    }
    return render(request, 'myapp/new_search.html', context=data_for_frontend)
