from random import randint
import requests
import time
import os

rapidapi_key = str(os.getenv('RAPIDAPI_KEY'))
rapidapi_host = str(os.getenv('RAPIDAPI_HOST'))

def handle_response(message):
    if message == '?help':
        return "type ! + a type of movie to suggest a movie"
    
    if message[0] == '!':
        p_message = message.lower().split('-')

        message_category = p_message[0][1:]

        url = "https://advanced-movie-search.p.rapidapi.com/genre/movie/list"
        headers = {
            "X-RapidAPI-Key": rapidapi_key,
            "X-RapidAPI-Host": rapidapi_host
        }
        response = requests.get(url, headers=headers).json()

        for cat in response['genres']:
            if cat['name'].lower() == message_category:
                category_id = cat['id']


        time.sleep(1)
        headers = {
            "X-RapidAPI-Key": rapidapi_key,
            "X-RapidAPI-Host": rapidapi_host
        }
        url = "https://advanced-movie-search.p.rapidapi.com/discover/movie"
        querystring = {"with_genres":category_id}
        response = requests.get(url, headers=headers, params=querystring).json()
        pages = response['total_pages']

        time.sleep(1)
        querystring = {"with_genres":category_id, "pages": pages}
        response = requests.get(url, headers=headers, params=querystring).json()

        position = randint(0, 20)
        return f"{response['results'][position]['title']} - {response['results'][position]['vote_average']}\n\n{response['results'][position]['overview']}"
