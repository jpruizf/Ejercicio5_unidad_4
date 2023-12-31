import json
from tkinter import messagebox
import urllib.request

class Modelo:
    __api_key: str
    def __init__(self):
        self.api_key = 'TU_API_KEY'
    
    def obtener_peliculas(self):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}"
        try:
            response = urllib.request.urlopen(url)
            data = json.load(response)
            return data['results']
        except urllib.error.URLError as e:
            messagebox.showerror("Error",f"Error al obtener las peliculas: {e}")
            return []
    
    def obtener_generos(self):
        generos_json = '''{"genres":[{"id":28,"name":"Action"},{"id":12,"name":"Adventure"},{"id":16,"name":"Animation"},{"id":35,"name":"Comedy"},{"id":80,"name":"Crime"},{"id":99,"name":"Documentary"},{"id":18,"name":"Drama"},{"id":10751,"name":"Family"},{"id":14,"name":"Fantasy"},{"id":36,"name":"History"},{"id":27,"name":"Horror"},{"id":10402,"name":"Music"},{"id":9648,"name":"Mystery"},{"id":10749,"name":"Romance"},{"id":878,"name":"Science Fiction"},{"id":10770,"name":"TV Movie"},{"id":53,"name":"Thriller"},{"id":10752,"name":"War"},{"id":37,"name":"Western"}]}'''
        data = json.loads(generos_json)
        return data["generos"]














