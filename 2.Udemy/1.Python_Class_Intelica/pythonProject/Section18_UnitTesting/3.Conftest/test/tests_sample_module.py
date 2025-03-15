import os
import sys

# Agregar el directorio raíz donde está sample_module.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import sample_module  # Ahora debería funcionar


def test_api_returns_data():
    actual = sample_module.get_api_data()
    expected = "MODIFIED DATA"

    assert actual == expected


def test_reverse_text(sample_text):
    actual = sample_module.reverse_text(sample_text)
    expected = "ananaB"
    assert actual == expected
