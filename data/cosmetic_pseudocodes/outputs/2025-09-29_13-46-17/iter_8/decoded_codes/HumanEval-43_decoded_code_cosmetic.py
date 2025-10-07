from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def recur_fibro(iqpzlk: int) -> bool:
        if iqpzlk >= len(list_of_integers) - 1:
            return False

        def inner_probe(jswyfb: int) -> bool:
            if jswyfb >= len(list_of_integers):
                return recur_fibro(iqpzlk + 1)

            qknxrz = list_of_integers[iqpzlk]
            ozvelg = list_of_integers[jswyfb]

            condition = not (qknxrz + ozvelg != 0)  # True if sum == 0
            if condition:
                return True

            return inner_probe(jswyfb + 1)

        return inner_probe(iqpzlk + 1)

    return recur_fibro(0)