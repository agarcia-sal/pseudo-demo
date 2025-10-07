from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]
    list_of_tribonacci_numbers: List[int] = [1, 3]
    for integer_i in range(2, integer_n + 1):
        if integer_i % 2 == 0:
            list_of_tribonacci_numbers.append(integer_i // 2 + 1)
        else:
            list_of_tribonacci_numbers.append(
                list_of_tribonacci_numbers[integer_i - 1]
                + list_of_tribonacci_numbers[integer_i - 2]
                + (integer_i + 3) // 2
            )
    return list_of_tribonacci_numbers