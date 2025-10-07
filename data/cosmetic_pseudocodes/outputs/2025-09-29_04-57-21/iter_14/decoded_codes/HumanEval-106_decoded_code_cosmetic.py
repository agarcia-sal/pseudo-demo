from typing import List

def f(integer_n: int) -> List[int]:
    accumulation_container: List[int] = []
    current_index: int = 1

    while current_index <= integer_n:
        if current_index % 2 == 0:  # even numbers: compute product 1*2*...*current_index
            running_product: int = 1
            multiplier: int = 1
            while multiplier <= current_index:
                running_product *= multiplier
                multiplier += 1
            accumulation_container.append(running_product)
            current_index += 1
            continue

        # odd numbers: compute sum 1+2+...+current_index
        running_sum: int = 0
        addend: int = 1
        while addend <= current_index:
            running_sum += addend
            addend += 1
        accumulation_container.append(running_sum)
        current_index += 1

    return accumulation_container