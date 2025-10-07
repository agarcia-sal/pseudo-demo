from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_multiplier = 1
        while integer_value < 0:
            integer_value = -integer_value
            sign_multiplier = -1

        digits_str = str(integer_value)
        digits_array: List[int] = []
        index = 0

        while True:
            if index >= len(digits_str):
                break
            digits_array.append(int(digits_str[index]))
            index += 1

        digits_array[0] *= sign_multiplier

        total = 0
        pos = 0
        while True:
            if pos >= len(digits_array):
                break
            total += digits_array[pos]
            pos += 1

        return total

    def helper(idx: int, acc: int) -> int:
        if idx == len(array_of_integers):
            return acc
        else:
            val = digits_sum(array_of_integers[idx])
            if val > 0:
                return helper(idx + 1, acc + 1)
            else:
                return helper(idx + 1, acc)

    return helper(0, 0)