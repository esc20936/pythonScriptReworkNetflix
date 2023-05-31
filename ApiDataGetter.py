# API call to get the data from the API
# and save it to a file

import requests
import json
import os
import datetime

# movies with errors
moviesWithErrorRequest = []

def save_data(data, file_name): 
    file_name = "generatedFiles/" + file_name
#    create a new file with the name of the movie and save the data to it
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
        
    
    
    
# API call to get the data from the API
# and save it to a file
def get_data(movie_name):
    # API url
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey=6c40a7d3"

    # API call
    response = requests.get(url)

    # check if the response is ok
    if response.status_code != 200:
        moviesWithErrorRequest.append(movie_name)
        print("Error in API call for movie: " + movie_name)
        return
    # get the data
    data = response.json()
    # create a unique file name for the movie using the title and the now date
    date = str(datetime.datetime.now()).replace('.','_').replace(":","_")
    newName = f"{movie_name}__{date}.json"
    # save the data to a file
    save_data(data, newName)
    
    print("Data saved for movie: " + movie_name)


movies = [
        "Casablanca",
    "Gone with the Wind",
    "Citizen Kane",
    "Lawrence of Arabia",
    "The Wizard of Oz",
    "Vertigo",
    "Seven Samurai",
    "Apocalypse Now",
    "Taxi Driver",
    "The Godfather: Part II",
    "The Shawshank Redemption",
    "Eternal Sunshine of the Spotless Mind",
    "Blade Runner",
    "The Big Lebowski",
    "Pulp Fiction",
    "The Grand Budapest Hotel",
    "The Dark Knight",
    "Fight Club",
    "Inception",
    "The Matrix",
    "Goodfellas",
    "The Departed",
    "The Green Mile",
    "No Country for Old Men",
    "The Social Network",
    "Birdman",
    "Whiplash",
    "La La Land",
    "Moonlight",
    "Parasite",
    "Joker",
    "1917",
    "The Irishman",
    "Knives Out",
    "Ford v Ferrari",
    "Jojo Rabbit",
    "Once Upon a Time in Hollywood",
    "Tenet",
    "Soul",
    "Promising Young Woman",
    "Minari",
    "Sound of Metal",
    "Nomadland",
    "Mank",
    "The Trial of the Chicago 7",
    "The Father",
    "Ma Rainey's Black Bottom",
    "The Midnight Sky",
    "Pieces of a Woman",
    "News of the World",
    "Synchronic",
    "The White Tiger",
    "Another Round",
    "The Dig",
    "I Care a Lot",
    "The Mauritanian",
    "Cherry",
    "Raya and the Last Dragon",
    "Cruella",
    "Luca",
    "The Mitchells vs. the Machines",
    "A Quiet Place Part II",
    "Black Widow",
    "F9",
    "Jungle Cruise",
    "Dune",
    "The Suicide Squad",
    "Spider-Man: No Way Home",
    "The French Dispatch",
    "Matrix 4",
    "Doctor Strange in the Multiverse of Madness",
    "Thor: Love and Thunder",
    "Black Panther: Wakanda Forever",
    "Mission: Impossible 7",
    "Avatar 2",
    "Jurassic World: Dominion",
    "The Batman",
    "Indiana Jones 5",
    # ... and so on, up to a total of 100 movie titles

]

for movie in movies:
    get_data(movie)
    
