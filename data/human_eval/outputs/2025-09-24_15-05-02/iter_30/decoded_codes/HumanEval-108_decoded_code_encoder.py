from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        neg = 1
        if number < 0:
            number = -number
            neg = -1
        digits_list = [int(d) for d in str(number)]
        digits_list[0] *= neg
        return sum(digits_list)

    digit_sums = [digits_sum(i) for i in array_of_integers]
    filtered_list = [x for x in digit_sums if x > 0]
    return len(filtered_list)