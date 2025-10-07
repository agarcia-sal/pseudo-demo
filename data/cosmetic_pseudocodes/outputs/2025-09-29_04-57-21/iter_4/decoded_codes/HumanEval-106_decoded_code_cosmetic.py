from typing import List


def f(number_limit: int) -> List[int]:
    output_sequence: List[int] = []
    current_index: int = 1
    while current_index <= number_limit:
        if current_index % 2 == 0:
            product_accumulator: int = 1
            multiplier: int = 1
            while multiplier <= current_index:
                product_accumulator *= multiplier
                multiplier += 1
            output_sequence.append(product_accumulator)
        else:
            total_sum: int = 0
            addend: int = 1
            while addend <= current_index:
                total_sum += addend
                addend += 1
            output_sequence.append(total_sum)
        current_index += 1
    return output_sequence