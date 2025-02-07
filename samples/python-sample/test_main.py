import pytest
from utils import greet


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


if __name__ == "__main__":
    pytest.main()
