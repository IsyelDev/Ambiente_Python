class Pelicula:
    def __init__(self, titulo: str, director: str, codigo: str, disponible: bool = True):
        self.titulo = titulo
        self.director = director
        self.codigo = codigo
        self.disponible = disponible

    def informacion(self):
        return f"""Titulo: {self.titulo}
Director: {self.director}
Codigo: {self.codigo}
Disponible: {"Sí" if self.disponible else "No"}"""

    def alquilar(self):
        if not self.disponible:
            return f"La película '{self.titulo}' ya está alquilada."
        self.disponible = False
        return f"La película '{self.titulo}' ha sido alquilada.\n\n{self.informacion()}"

    def devolver(self):
        if self.disponible:
            return f"La película '{self.titulo}' ya está en la videoteca."
        self.disponible = True
        return f"La película '{self.titulo}' fue devuelta.\n\n{self.informacion()}"


# Instancias
pelicula1 = Pelicula("Inception", "Christopher Nolan", "C001")
pelicula2 = Pelicula("Interstellar", "Christopher Nolan", "C002")

# Pruebas
print(pelicula1.alquilar())
print(pelicula1.devolver())
print(pelicula1.alquilar())
print(pelicula1.devolver())

print(pelicula2.alquilar())
print(pelicula2.devolver())
print(pelicula2.alquilar())
print(pelicula2.devolver())
