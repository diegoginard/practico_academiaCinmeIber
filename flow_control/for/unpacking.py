# Libros de Brandon Sanderson

books = [
    "Elantris, Brandon Sanderson, 2005",
    "El camino de los reyes, Brandon Sanderson, 2010",
    "Palabras radiantes, Brandon Sanderson, 2014",
    "Juramentada, Brandon Sanderson, 2017",
    "El aliento de los dioses, Brandon Sanderson, 2019",
    "Rhythm of War, Brandon Sanderson, 2020",
]

# for book in books:
#     title, author, year = book.split(", ")
#     print(f"El libro {title} fue escrito por {author} en el año {year}")

# Ejemplo omitiendo el autor

# for book in books:
#     title, _, year = book.split(", ")
#     print(f"El libro {title} fue escrito en el año {year}")

# Ejemplo de unpacking con el operador de desempaquetado

for book in books:
    title, *_ = book.split(", ")
    print(f"La bibliografía de Brandon Sanderson incluye los libros {title}")
