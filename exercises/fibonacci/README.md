# Exercise: Fibonacci Numbers

*[Leer en Español](README.es.md)*

## Background/Motivation

The Fibonacci sequence is one of the most famous sequences in mathematics. It appears in nature, art, and architecture, and is a fundamental example of recursion and iterative growth in computer science. Understanding how to generate this sequence is a core skill for any programmer.

## The Task

Implement a function `fibonacci(n: int) -> int` that calculates the $n$-th number in the Fibonacci sequence. The sequence is defined as:

- $F(0) = 0$
- $F(1) = 1$
- $F(n) = F(n-1) + F(n-2)$ for $n \ge 2$

### Specifications

- **Function Name**: `fibonacci`
- **Arguments**: `n` (int)
- **Return Type**: `int`
- **Expected Output**: The $n$-th Fibonacci number.

### Constraints

- $0 \le n \le 30$
- Your implementation must be efficient enough to calculate $F(30)$ within standard time limits.

### Example

```python
>>> fibonacci(5)
5
>>> fibonacci(10)
55
```

## Instructions

1. Open `exercises/fibonacci/solution.py`.
2. Implement the `fibonacci` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
