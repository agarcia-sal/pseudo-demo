from typing import List

def f(integer_n: int) -> List[int]:
    output_array: List[int] = []
    counter_i: int = 1
    while counter_i <= integer_n:
        if counter_i % 2 == 0:
            product: int = 1
            counter_j: int = 1
            while counter_j <= counter_i:
                product *= counter_j
                counter_j += 1
            output_array.append(product)
        else:
            total_sum: int = 0
            counter_j: int = 1
            while counter_j <= counter_i:
                total_sum += counter_j
                counter_j += 1
            output_array.append(total_sum)
        counter_i += 1
    return output_array