from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_n: int) -> int:
        neg = 1
        if integer_n < 0:
            integer_n = -integer_n
            neg = -1
        digits = [int(d) for d in str(integer_n)]
        digits[0] *= neg
        return sum(digits)

    digit_sums: List[int] = [digits_sum(i) for i in array_of_integers]
    filtered_list = [ds for ds in digit_sums if ds > 0]
    return len(filtered_list)