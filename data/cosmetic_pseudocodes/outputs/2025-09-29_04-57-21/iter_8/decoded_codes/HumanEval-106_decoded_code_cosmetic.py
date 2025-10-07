from typing import List

def f(integer_n: int) -> List[int]:
    output_collection: List[int] = []
    current_number: int = 1

    while current_number <= integer_n:
        if not (current_number % 2 != 0):  # current_number is even
            prod_result: int = 1
            multiplier: int = 1
            while multiplier <= current_number:
                prod_result *= multiplier
                multiplier += 1
            output_collection.append(prod_result)
        else:
            accum_sum: int = 0
            term: int = 1
            while True:
                accum_sum += term
                term += 1
                if term > current_number:
                    break
            output_collection.append(accum_sum)

        current_number += 1

    return output_collection