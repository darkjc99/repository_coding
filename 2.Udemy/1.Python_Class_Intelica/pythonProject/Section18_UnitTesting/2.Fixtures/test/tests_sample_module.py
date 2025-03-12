import pytest
import sample_module  # Ahora debería funcionar


def test_sort_numbers():
    numbers = [9, 5, -1, -10, 10]
    actual = sample_module.sort_numbers(numbers)
    expected = [-10, -1, 5, 9, 10]
    assert actual == expected


def test_reverse_numbers():
    numbers = [9, 5, -1, -10, 10]
    actual = sample_module.reverse_numbers(numbers)
    expected = []
    assert actual == expected
