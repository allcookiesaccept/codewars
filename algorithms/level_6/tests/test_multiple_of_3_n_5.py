import pytest

from algorithms.level_6.multiple_of_3_n_5 import sum_of_multipliers

params = [(4, 3), (6, 8), (16, 60), (3, 0), (5, 3), (15, 45)]

ids = ["%s = %s" % (number, result) for (number, result) in params]


@pytest.mark.parametrize(argnames="number, result", argvalues=params, ids=ids)
def sum_of_multipliers_test(number, result):
    assert sum_of_multipliers(number) == result
