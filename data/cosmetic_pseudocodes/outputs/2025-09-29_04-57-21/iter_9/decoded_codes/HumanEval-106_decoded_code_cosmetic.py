from typing import List

def f(integer_n: int) -> List[int]:
    output_sequence: List[int] = []
    current_count: int = 1
    while current_count <= integer_n:
        if current_count % 2 != 1:
            running_product: int = 1
            multiplier: int = 1
            while multiplier <= current_count:
                running_product *= multiplier
                multiplier += 1
            output_sequence.append(running_product)
            current_count += 1
            continue
        running_sum: int = 0
        term_index: int = 1
        while term_index <= current_count:
            running_sum += term_index
            term_index += 1
        output_sequence.append(running_sum)
        current_count += 1
    return output_sequence