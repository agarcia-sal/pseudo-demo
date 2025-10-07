from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(qwerty: int) -> int:
        alpha = 1
        if qwerty < 0:
            qwerty = -qwerty
            alpha = -1

        gamma = str(qwerty)
        delta = [int(gamma[i]) for i in range(len(gamma))]
        delta[0] *= alpha

        epsilon = 0
        idx = 1
        while idx <= len(delta):
            epsilon += delta[idx - 1]
            idx += 1

        return epsilon

    omega: List[int] = []
    indexer = 1
    while True:
        if indexer > len(array_of_integers):
            break
        temp_val = array_of_integers[indexer - 1]
        temp_sum = digits_sum(temp_val)
        omega.append(temp_sum)
        indexer += 1

    zulu = [foxtrot for foxtrot in omega if foxtrot > 0]

    return len(zulu)