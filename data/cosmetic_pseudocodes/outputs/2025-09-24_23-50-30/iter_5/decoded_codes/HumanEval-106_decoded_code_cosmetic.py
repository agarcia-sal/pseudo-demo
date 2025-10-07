from typing import List

def f(k: int) -> List[int]:
    def accumulate_sum(m: int, acc: int) -> int:
        if m < 1:
            return acc
        return accumulate_sum(m - 1, acc + m)

    def accumulate_product(m: int, acc: int) -> int:
        if m < 1:
            return acc
        return accumulate_product(m - 1, acc * m)

    output_collection: List[int] = []

    def process_element(x: int) -> int:
        if x % 2 == 0:
            return accumulate_product(x, 1)
        return accumulate_sum(x, 0)

    index = 1
    while index <= k:
        output_collection.append(process_element(index))
        index += 1

    return output_collection