import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import sample_module as sm


@pytest.fixture()
def sample_text() -> str:
    return "Banana"


@pytest.fixture(autouse=True)
def disable_api_data():
    sm.get_api_data = lambda: "MODIFIED DATA"
