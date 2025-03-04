# Agente de Recomendación de Películas

Este agente recomienda películas basándose en el género favorito del usuario. Utiliza un diccionario de películas organizadas por género y selecciona una recomendación aleatoria.

### Funcionamiento

1. **Diccionario de Películas**:
   - Las películas están organizadas por género: acción, comedia, drama, ciencia ficción y terror.

2. **Interacción con el Usuario**:
   - El usuario ingresa su género favorito.
   - El programa verifica si el género existe en el diccionario.

3. **Recomendación Aleatoria**:
   - Si el género es válido, el programa selecciona una película aleatoria del género.
   - Si el género no es válido, muestra un mensaje de error.

### Ejecución

Para ejecutar el programa, usa el siguiente comando:

```bash
python recomendador_peliculas.py