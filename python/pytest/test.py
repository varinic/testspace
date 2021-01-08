

#!/usr/bin/env python3

import pytest

@pytest.fixture
def data():

    return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]

def test_fixture(data):
    assert len(data) == 10
