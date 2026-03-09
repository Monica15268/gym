# Exercise: Fibonacci Numbers

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.

## The Task

Implement a function `fibonacci(n: int) -> int` that calculates the $n$-th number in the Fibonacci sequence.

### Sequence Definition

The sequence starts as follows:

$F(0) = 0$
$F(1) = 1$
$F(n) = F(n-1) + F(n-2)$ for $n \ge 2$

The sequence begins: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...$

### Specifications

- **Function Name**: `fibonacci`
- **Arguments**: `n` (an integer, where $0 \le n \le 30$)
- **Return Type**: `int`

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
3. Run `make test` locally to verify your solution.
