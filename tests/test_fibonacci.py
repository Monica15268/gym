import pytest
from exercises.fibonacci import solution
from exercises.fibonacci.solution import fibonacci

if not getattr(solution, "SUBMIT", False):
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_fibonacci_base_case_zero() -> None:
    """Check if fibonacci(0) returns 0."""
    assert fibonacci(0) == 0


def test_fibonacci_base_case_one() -> None:
    """Check if fibonacci(1) returns 1."""
    assert fibonacci(1) == 1


def test_fibonacci_two() -> None:
    """Check if fibonacci(2) returns 1."""
    assert fibonacci(2) == 1
