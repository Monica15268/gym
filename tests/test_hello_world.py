import pytest
from exercises.hello_world import solution
from exercises.hello_world.solution import hello_world

if not getattr(solution, "SUBMIT", False):
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_hello_world_callable() -> None:
    """Check if the function exists and is callable."""
    assert callable(hello_world)


def test_hello_world_return_type() -> None:
    """Check if the return value is a string."""
    assert isinstance(hello_world(), str)
