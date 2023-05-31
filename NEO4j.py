import logging

from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError
from datetime import datetime

def convertStringToDate(dateString):
    res = datetime.strptime(dateString, '%d %b %Y')
    return res

def separateStringByComma(string):
    res = string.split(",")
    return list(res)



class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print("Connected to Neo4j")

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()


    def create_genre_movie_relationship(self, genre_name, movie_name):
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(
                self._create_and_return_relationship2, genre_name, movie_name)
            for record in result:
                print("Created relationship: {relationship}".format(
                    relationship=record['relationship']))
    
    @staticmethod
    def _create_and_return_relationship2(tx, genre_name, movie_name):
        
        result = tx.run("MATCH (g:Genre {name:$genre_name}) "
                        "MATCH (m:Movie {title:$movie_name}) "
                        "MERGE (g)-[r:GENRE_OF]->(m) "
                        "RETURN g.name, type(r), m.title", genre_name=genre_name, movie_name=movie_name)
        try:
            return [{"genre": record["g.name"], "relationship": record["type(r)"], "movie": record["m.title"]} for record in result]
        except Neo4jError as error:
            logging.error(error)
            return []



    def create_genre(self, genre_name):
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(
                self._create_and_return_genre, genre_name)
            for record in result:
                print("Created genre: {genre}".format(
                    genre=record['genre']))
            
    @staticmethod
    def _create_and_return_genre(tx, genre_name):
        result = tx.run("MERGE (g:Genre {name: $genre_name}) "
                        "RETURN g.name AS genre", genre_name=genre_name)
        try:
            return [{"genre": record["genre"]} for record in result]
        except Neo4jError as error:
            logging.error(error)
            return []

    
    def create_person_movie_relationship(self, person_name, movie_name, role,year):
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(
                self._create_and_return_relationship, person_name, movie_name, role,year)
            for record in result:
                print("Created relationship: {relationship}".format(
                    relationship=record['relationship']))
                
    @staticmethod
    def _create_and_return_relationship(tx, person_name, movie_name, relationship,year):
        query = ""
        if relationship == "ACTED_IN":
            
            query = (
                "MATCH (p:Person {name:$person_name}) "
                "MATCH (m:Movie {title:$movie_name}) "
                "MERGE (p)-[r:ACTED_IN {year:$year}]->(m)"
                "RETURN r"
            )
        else:
            query = (
                "MATCH (p:Person {name:$person_name}) "
                "MATCH (m:Movie {title:$movie_name}) "
                "MERGE (p)-[r:DIRECTED {year:$year}]->(m)"
                "RETURN r"
            )
        result = tx.run(query, person_name=person_name, movie_name=movie_name, relationship=relationship,year=year)
        try:
            return [{"relationship": record["r"]} for record in result]
        except Neo4jError as error:
            logging.error(error)
            return []
    
    
    def create_person(self, person_name):
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(
                self._create_and_return_person, person_name)
            for record in result:
                print("Created person: {person}".format(
                    person=record['person']))
    
    @staticmethod
    def _create_and_return_person(tx, person_name):
        query = (
            "MERGE (p:Person {name:$name})"
            "RETURN p"
        )
        result = tx.run(query, name=person_name)
        try:
            return [{"person": record["p"]["name"]} for record in result]
        except Neo4jError as error:
            logging.error(error)
            return []
    
    def create_movie(self, movie_name, movie_data):
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(
                self._create_and_return_movie, movie_name, movie_data)
            for record in result:
                print("Created movie: {movie}".format(
                    movie=record['movie']))
                
    @staticmethod
    def _create_and_return_movie(tx, movie_name, movie_data):
        # spread movie data
        title = movie_data["Title"]
        year = int(movie_data["Year"])
        rated = movie_data["Rated"]
        released =  convertStringToDate(movie_data["Released"])
        runtime = movie_data["Runtime"]
        poster = movie_data["Poster"]
        imdbRating = float(movie_data["imdbRating"])
        countries = separateStringByComma(movie_data["Country"])
        typeMovie = True if movie_data["Type"] == "movie" else False
        plot = movie_data["Plot"]
        query = (
            "MERGE (m:Movie {title:$title,plot:$plot, year:$year, rated:$rated, released:date($released), runtime:$runtime, poster:$poster, imdbRating:$imdbRating, countries:$countries, typeMovie:$typeMovie})"
            "RETURN m"
        )
        result = tx.run(query, title=title,plot=plot, year=year, rated=rated, released=released, runtime=runtime, poster=poster, imdbRating=imdbRating, countries=countries, typeMovie=typeMovie)
        try:
            return [{"movie": record["m"]["title"]} for record in result]
        except Neo4jError as error:
            logging.error(error)
            return []

  