from typing import List


def f(number_limit: int) -> List[int]:
    storage: List[int] = []
    index_counter: int = 1
    while index_counter <= number_limit:
        current_step: int = index_counter
        if current_step % 2 != 1:  # even number
            accum_product: int = 1
            multiplier: int = 1
            while multiplier <= current_step:
                accum_product *= multiplier
                multiplier += 1
            storage.append(accum_product)
        else:
            accum_sum: int = 0
            addend: int = 1
            while addend <= current_step:
                accum_sum += addend
                addend += 1
            storage.append(accum_sum)
        index_counter += 1
    return storage