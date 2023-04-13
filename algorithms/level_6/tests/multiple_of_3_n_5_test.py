import pytest

from algorithms.level_6.multiple_of_3_n_5 import sum_of_multipliers


@pytest.mark.parametrize("number, result",
                         [(4, 3), (6, 8), (16, 60), (3, 0), (5, 3), (15, 45)])
def sum_of_multipliers_test(number, result):
    assert sum_of_multipliers(number) == result
