
def _min(list_numbers: list) -> int:
    """Function find minimum number in list numbers"""

    min_number = list_numbers[0]
    for number in list_numbers[1:]:
        if number < min_number:
            min_number = number
    return min_number

# @pytest.mark.parametrize('list_num, result', [([12, 3, 4, 5, 0], 0),
#                                           ([-1, -7, 2], -7),
#                                           ([1], 1),
#                                           ([2, 2, 2, 2, 1, 2]),
#                                           ])
def test_min_func_1():
    assert _min([12, 3, 4, 5, 0]) == 0


def test_min_func_2():
    assert _min([0]) == 0


def test_min_func_3():
    assert _min([-12, 3, 4, 5, 0]) == -12
