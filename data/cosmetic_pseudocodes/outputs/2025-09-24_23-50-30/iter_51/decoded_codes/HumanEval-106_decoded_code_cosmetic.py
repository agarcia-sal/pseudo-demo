from typing import List


def f(integer_n: int) -> List[int]:
    def compute_sum(accumulator: int, limit: int, cursor: int) -> int:
        if cursor > limit:
            return accumulator
        return compute_sum(accumulator + cursor, limit, cursor + 1)

    def compute_product(accumulator: int, limit: int, cursor: int) -> int:
        if cursor > limit:
            return accumulator
        return compute_product(accumulator * cursor, limit, cursor + 1)

    output_collection: List[int] = []

    def process_index(current_index: int) -> None:
        if current_index > integer_n:
            return
        if current_index % 2 == 0:
            value = compute_product(1, current_index, 1)
        else:
            value = compute_sum(0, current_index, 1)
        output_collection.append(value)
        process_index(current_index + 1)

    process_index(1)
    return output_collection