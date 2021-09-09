import pytest

def sum(a, b):
    return a + b

@pytest.mark.parametrize("input1, input2, output", [(5, 5, 10), (2, 3, 5)])
def test_calculate_sum_1(input1, input2, output):
    result = sum(input1, input2)
    assert result == output