from random import randint
import requests
import time

def handle_response(message):
    if message == '?help':
        return "type ! + a type of movie to suggest a movie"
    
    if message[0] == '!':
        p_message = message.lower().split('-')

        message_category = p_message[0][1:]

        url = "https://advanced-movie-search.p.rapidapi.com/genre/movie/list"
        headers = {
            "X-RapidAPI-Key": "e0034ad13fmshd9c514fcd352d4fp1dcda1jsn5aa0116e1745",
            "X-RapidAPI-Host": "advanced-movie-search.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers).json()

        for cat in response['genres']:
            if cat['name'].lower() == message_category:
                category_id = cat['id']


        time.sleep(1)
        headers = {
            "X-RapidAPI-Key": "e0034ad13fmshd9c514fcd352d4fp1dcda1jsn5aa0116e1745",
            "X-RapidAPI-Host": "advanced-movie-search.p.rapidapi.com"
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
