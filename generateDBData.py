from NEO4j import App
import os
def getJSONData(fileName):
    import json
    fileName = "generatedFiles/" + fileName
    with open(fileName) as json_file:
        data = json.load(json_file)
    return data


def generateMovieNodes(app):
    # iterate over the files in the folder generatedFiles
    for file in os.listdir("generatedFiles"):
        try:
            # get the data from the file
            data = getJSONData(file)
            # get the movie name
            movieName = data["Title"]
            # create the movie node
            app.create_movie(movieName, data)
        except:
            print("Error in file: " + file)
            continue

def generatePersonNodes(app):
    # iterate over the files in the folder generatedFiles
    for file in os.listdir("generatedFiles"):
        try:
            # get the data from the file
            data = getJSONData(file)
            # get the movie name
            actors = data["Actors"].split(",")
            directors = data["Director"].split(",")
            
            for actor in actors:
                app.create_person(actor.strip())
            for director in directors:
                app.create_person(director.strip())
            
            # create the movie node
            # app.create_movie(movieName, data)
        except:
            print("Error in file: " + file)
            continue

def generateRelationships(app):
    for file in os.listdir("generatedFiles"):
        try:
            # get the data from the file
            data = getJSONData(file)
            # get the movie name
            movieName = data["Title"]
            # get the actors and directors
            actors = data["Actors"].split(",")
            directors = data["Director"].split(",")
            year = int(data["Year"])
            # create the relationships
            for actor in actors:
                app.create_person_movie_relationship(actor.strip(), movieName, "ACTED_IN",year)
            for director in directors:
                app.create_person_movie_relationship(director.strip(), movieName, "DIRECTED",year)
            
            # create the movie node
            # app.create_movie(movieName, data)
        except:
            print("Error in file: " + file)
            continue

def createGenre(app):
    for file in os.listdir("generatedFiles"):
        try:
            # get the data from the file
            data = getJSONData(file)
            # get the movie name
            movieName = data["Title"]
            # get the actors and directors
            genre = data["Genre"].split(",")
            # create the relationships
            for g in genre:
                app.create_genre(g.strip())
            
            # create the movie node
            # app.create_movie(movieName, data)
        except:
            print("Error in file: " + file)
            continue


def createMovieGenreRelationShip(app):
    for file in os.listdir("generatedFiles"):
        try:
            # get the data from the file
            data = getJSONData(file)
            # get the movie name
            movieName = data["Title"]
            # get the actors and directors
            genre = data["Genre"].split(",")
            # create the relationships
            for g in genre:
                app.create_genre_movie_relationship(g.strip(),movieName )
            
            # create the movie node
            # app.create_movie(movieName, data)
        except Exception as e:
            # print the error
            print(e)
            continue


if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://ffdacf65.databases.neo4j.io"
    user = "neo4j"
    password = "sFlE8EchqCO2xYZ1iqbXQ4y5neW9GJFtwVwQLCj-L1I"
    app = App(uri, user, password)
   
    # generateMovieNodes(app)
    # generatePersonNodes(app)
    # generateRelationships(app)
    # createGenre(app)
    createMovieGenreRelationShip(app)
    
    app.close() 
    
    # fileName = "1917__2023-05-26 20_32_24_764963.json"
    
    # data = getJSONData(fileName)
    # movieName = data["Title"]
    # app.create_movie(movieName, data)
    # app.close()
    
    