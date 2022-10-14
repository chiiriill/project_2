def read_txt_file(filename: str) -> list:
    """Function read txt file and give list numbers"""

    with open(filename, 'r') as file_:
        # print(f'В файле: {file_.read()}')
        return [int(number) for number in file_.read().split()]


def _min(list_numbers: list) ->  int:
    """Function find minimum number in list numbers"""

    min_number = list_numbers[0]
    for number in list_numbers[1:]:
        if number < min_number:
            min_number = number
    return min_number


def _max(list_numbers: list) -> int:
    """Function find maximum number in list numbers"""

    max_number = list_numbers[0]
    for number in list_numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number


def _sum(list_numbers: list) -> int:
    """Function find summary numbers"""

    result = 0
    for number in list_numbers:
        result += number
    return result


def _mul(list_numbers: list) -> int:
    """Function find mul numbers"""

    result = 1
    for number in list_numbers:
        result *= number
    return result


def main(filename: str):
    numbers = read_txt_file(filename)
    print(numbers)
    print(f'Минимальное: {_min(numbers)}')
    print(f'Максимальное: {_max(numbers)}')
    print(f'Сумма {_sum(numbers)}')
    print(f'Произведение: {_mul(numbers)}')


if __name__ == '__main__':
    filename = input('Please input filename: ')
    main(filename)
