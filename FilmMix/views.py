from django.shortcuts import render
import random 
import csv
import json
import requests

# Create your views here.
def filmRecomendation(request):
    random_choice = random.randint(0, len(list_of_films))
    film = list_of_films[random_choice] 
    year = list_of_years[random_choice]
    uri = list_of_uri[random_choice]

    titles['s'] = film
    titles['y'] = year
    r = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=e0f2e12c', titles)
    movie_data = json.loads(r.text)
    poster_url = movie_data['Search'][0]['Poster']

    context = {
        'film' : film, 
        'year' : year,
        'uri' : uri,
        'poster_url' : poster_url
    }
    
    return render(request, 'FilmMix/filmmix.html', context)

list_of_films = []
list_of_uri = []
list_of_years = []
titles ={} 

with open('/home/Ingrid/Downloads/watchlist-_adenium-2023-12-12-05-04-utc.csv') as file_object:
    file_dict = csv.DictReader(file_object)
    for row in file_dict:
        list_of_films.append(row['Name'])
        list_of_years.append(row['Year'])
        list_of_uri.append(row['Letterboxd URI'])



