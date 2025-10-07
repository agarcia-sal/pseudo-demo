from typing import List

def f(integer_n: int) -> List[int]:
    output_collection: List[int] = []
    current_index: int = 1
    while current_index <= integer_n:
        if current_index % 2 == 0:
            prod_accumulator = 1
            multiplier = 1
            while multiplier <= current_index:
                prod_accumulator *= multiplier
                multiplier += 1
            output_collection.append(prod_accumulator)
        else:
            sum_accumulator = 0
            addend = 1
            while addend <= current_index:
                sum_accumulator += addend
                addend += 1
            output_collection.append(sum_accumulator)
        current_index += 1
    return output_collection