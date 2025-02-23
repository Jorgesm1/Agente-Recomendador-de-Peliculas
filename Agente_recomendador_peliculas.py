import random

def recomendador_peliculas():
    # Diccionario de películas organizadas por género
    peliculas_por_genero = {
        "acción": ["Mad Max: Fury Road", "John Wick", "The Dark Knight", "Inception", "Gladiator"],
        "comedia": ["Superbad", "The Hangover", "Bridesmaids", "Dumb and Dumber", "Step Brothers"],
        "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Schindler's List", "Fight Club"],
        "ciencia ficción": ["Blade Runner 2049", "Interstellar", "The Matrix", "Inception", "Star Wars: Episode V"],
        "terror": ["The Conjuring", "Hereditary", "Get Out", "The Exorcist", "A Quiet Place"]
    }

    print("Bienvenido al Agente de Recomendación de Películas")
    print("Géneros disponibles: acción, comedia, drama, ciencia ficción, terror")

    # Solicitar género favorito al usuario
    genero_favorito = input("¿Cuál es tu género favorito? ").strip().lower()

    # Verificar si el género existe en el diccionario
    if genero_favorito in peliculas_por_genero:
        # Seleccionar una película aleatoria del género favorito
        pelicula_recomendada = random.choice(peliculas_por_genero[genero_favorito])
        print(f"\nRecomendación: Deberías ver '{pelicula_recomendada}'.")
    else:
        print("\nLo siento, no tenemos recomendaciones para ese género.")

if __name__ == "__main__":
    recomendador_peliculas()