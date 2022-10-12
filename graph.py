import matplotlib.pyplot as plt
from random import randint
import practik_2
import time


# dictionary = {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
# }

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# plt.plot(list(dictionary.keys()), list(dictionary.values()))
# plt.show()

def create_file_with_number(amount_number: int):
    with open(file='base.txt', mode='w') as file_:
        file_.write(' '.join([str(randint(-100, 100)) for _ in range(amount_number)]))


def main():
    base_data = dict()
    for amount_number in range(1, 1000, 10):
        start_time = time.time()
        create_file_with_number(amount_number)
        practik_2.main('base.txt')
        base_data[amount_number] = time.time() - start_time
    plt.plot(list(base_data.keys()), list(base_data.values()))
    plt.show()

if __name__ == '__main__':
    main()
