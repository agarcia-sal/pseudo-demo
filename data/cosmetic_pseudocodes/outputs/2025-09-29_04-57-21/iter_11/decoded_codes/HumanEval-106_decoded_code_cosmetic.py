from typing import List

def f(integer_n: int) -> List[int]:
    collection_result: List[int] = []
    counter_a: int = 1
    while counter_a <= integer_n:
        if (counter_a % 2) != 1:  # even number
            product_accumulator: int = 1
            counter_b: int = 1
            while counter_b <= counter_a:
                product_accumulator *= counter_b
                counter_b += 1
            collection_result.append(product_accumulator)
        else:
            sum_accumulator: int = 0
            counter_b = 1
            while counter_b <= counter_a:
                sum_accumulator += counter_b
                counter_b += 1
            collection_result.append(sum_accumulator)
        counter_a += 1
    return collection_result