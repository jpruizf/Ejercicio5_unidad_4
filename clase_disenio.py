import tkinter as tkk
from tkinter import messagebox
class Vista:
    __controlador: object
    __listbox:list
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tkk.Tk()
        self.ventana.title('Cinefilos Argentinos')

        self.__listbox = tkk.Listbox(self.ventana)
        self.__listbox.pack()
        peliculas = self.__controlador.obtener_peliculas()
        for pelicula in peliculas:
            self.__listbox.insert(tkk.END, pelicula['title'])

        self.__listbox.bind("<Double-Button-1>",self.mostrar_datos)
        self.ventana.mainloop()

    def mostrar_datos(self):
        seleccion = self.__listbox.get(self.__listbox.curselection())
        peliculas = self.__controlador.obtener_peliculas()
        generos = self.__controlador.obtener_generos()
        for pelicula in peliculas:
            if pelicula['title'] == seleccion:
                generos_nombres = [genero['name']for genero in generos if genero['id'] in pelicula['genre_ids']]
                messagebox.showinfo("Informacion de la pelicula", f"Titulo: {pelicula['title']}\nResumen: {pelicula['overview']}\nLenguaje original: {pelicula['original_lenguaje']}\nFecha de lanzamiento: {pelicula['release_date']}\nGeneros: {generos_nombres}")