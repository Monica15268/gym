# Ejercicio: Palíndromo

*[Read in English](README.md)*

## Antecedentes/Motivación

Un palíndromo es una palabra, frase, número u otra secuencia de caracteres que se lee igual hacia adelante que hacia atrás (ignorando espacios, puntuación y capitalización en algunos casos). En informática, determinar si una cadena es un palíndromo es un ejercicio clásico de manipulación de cadenas y lógica de punteros.

## La Tarea

Implementa una función `palindrome(text: str) -> bool` que verifique si una cadena dada es un palíndromo. Para este ejercicio, consideraremos la cadena exacta, lo que significa que las mayúsculas y los caracteres importan.

### Especificaciones

- **Nombre de la Función**: `palindrome`
- **Argumentos**: `text` (str)
- **Tipo de Retorno**: `bool`
- **Resultado Esperado**: `True` si la cadena es un palíndromo, `False` en caso contrario.

### Restricciones

- La cadena de entrada contendrá solo caracteres ASCII.
- $0 \le \text{len(text)} \le 1000$

### Ejemplo

```python
>>> palindrome("racecar")
True
>>> palindrome("hello")
False
>>> palindrome("aba")
True
```

## Instrucciones

1. Abre `exercises/palindrome/solution.py`.
2. Implementa la función `palindrome`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
