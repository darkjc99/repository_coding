import os
import sys

# Agregar el directorio raíz donde está sample_module.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import sample_module  # Ahora debería funcionar


@pytest.fixture()
def sample_numbers_unsorted() -> list[int]:
    return [-1, 3, 2, 1, 0]


def test_sort_numbers(sample_numbers_unsorted):
    actual = sample_module.sort_numbers(sample_numbers_unsorted)
    expected = [-1, 0, 1, 2, 3]
    assert actual == expected


def test_reverse_numbers(sample_numbers_unsorted):
    actual = sample_module.reverse_numbers(sample_numbers_unsorted)
    expected = [0, 1, 2, 3, -1]
    assert actual == expected
