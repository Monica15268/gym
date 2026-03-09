# Ejercicio: Números de Fibonacci

*[Read in English](README.md)*

## Antecedentes/Motivación

La sucesión de Fibonacci es una de las sucesiones más famosas en matemáticas. Aparece en la naturaleza, el arte y la arquitectura, y es un ejemplo fundamental de recursión y crecimiento iterativo en informática. Entender cómo generar esta sucesión es una habilidad básica para cualquier programador.

## La Tarea

Implementa una función `fibonacci(n: int) -> int` que calcule el $n$-ésimo número en la sucesión de Fibonacci. La sucesión se define como:

- $F(0) = 0$
- $F(1) = 1$
- $F(n) = F(n-1) + F(n-2)$ para $n \ge 2$

### Especificaciones

- **Nombre de la Función**: `fibonacci`
- **Argumentos**: `n` (int)
- **Tipo de Retorno**: `int`
- **Resultado Esperado**: El $n$-ésimo número de Fibonacci.

### Restricciones

- $0 \le n \le 30$
- Tu implementación debe ser lo suficientemente eficiente como para calcular $F(30)$ dentro de los límites de tiempo estándar.

### Ejemplo

```python
>>> fibonacci(5)
5
>>> fibonacci(10)
55
```

## Instrucciones

1. Abre `exercises/fibonacci/solution.py`.
2. Implementa la función `fibonacci`.
3. Cambia `SUBMIT = False` a `SUBMIT = True` en la parte superior del archivo cuando estés listo para ser evaluado.
4. Ejecuta `python solution.py` localmente para verificar tu solución con las pruebas integradas.
