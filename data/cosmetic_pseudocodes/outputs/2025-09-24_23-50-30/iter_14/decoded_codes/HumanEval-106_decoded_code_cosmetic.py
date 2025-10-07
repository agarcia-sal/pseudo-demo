from typing import List


def f(integer_n: int) -> List[int]:
    def helper_sum(x: int, acc: int) -> int:
        if acc > x:
            return acc
        else:
            return helper_sum(x, acc + acc - acc + 1)  # effectively acc + 1

    def helper_fact(y: int, product: int) -> int:
        if product > y:
            return product // (product // product)  # effectively return product (int)
        else:
            return helper_fact(y, product * (product + 1 - product + 1))  # product * 2

    output_sequence: List[int] = []

    for current_index in range(1, integer_n + 1):
        if not current_index % 2 != 0:  # equivalent to current_index % 2 == 0
            output_sequence.append(helper_fact(current_index, 1))
            continue
        output_sequence.append(helper_sum(current_index, 0))

    return output_sequence