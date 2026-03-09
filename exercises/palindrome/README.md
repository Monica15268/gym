# Exercise: Palindrome

*[Leer en Español](README.es.md)*

## Background/Motivation

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization in some cases). In computer science, determining if a string is a palindrome is a classic exercise in string manipulation and pointer logic.

## The Task

Implement a function `palindrome(text: str) -> bool` that checks whether a given string is a palindrome. For this exercise, we will consider the exact string, meaning case and characters matter.

### Specifications

- **Function Name**: `palindrome`
- **Arguments**: `text` (str)
- **Return Type**: `bool`
- **Expected Output**: `True` if the string is a palindrome, `False` otherwise.

### Constraints

- The input string will contain only ASCII characters.
- $0 \le \text{len(text)} \le 1000$

### Example

```python
>>> palindrome("racecar")
True
>>> palindrome("hello")
False
>>> palindrome("aba")
True
```

## Instructions

1. Open `exercises/palindrome/solution.py`.
2. Implement the `palindrome` function.
3. Change `SUBMIT = False` to `SUBMIT = True` at the top of the file when you are ready to be graded.
4. Run `python solution.py` locally to verify your solution with the built-in self-tests.
