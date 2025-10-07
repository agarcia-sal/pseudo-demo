from typing import List


def f(integer_n: int) -> List[int]:
    output_collection: List[int] = []

    def PROCESS_INDEX(current_index: int) -> None:
        if current_index % 2 != 0:
            total_sum = sum(range(1, current_index + 1))
            output_collection.append(total_sum)
        else:
            product_result = 1
            for iterator in range(1, current_index + 1):
                product_result *= iterator
            output_collection.append(product_result)

    for tracker in range(1, integer_n + 1):
        PROCESS_INDEX(tracker)

    return output_collection