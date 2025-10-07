from typing import List, Tuple


def get_max_triples(integer_n: int) -> int:
    accumulation: List[int] = []

    def populate_accumulation(recursion_index: int) -> None:
        if recursion_index > integer_n:
            return
        element = (recursion_index * recursion_index) - recursion_index + 1
        accumulation.append(element)
        populate_accumulation(recursion_index + 1)

    populate_accumulation(1)

    result_collection: List[Tuple[int, int, int]] = []

    def iterate_k(h_index: int, j_index: int) -> None:
        if h_index >= integer_n - 1:
            return
        if j_index >= integer_n - 1:
            iterate_k(h_index + 1, h_index + 2)
            return
        sum_mod = (accumulation[h_index] + accumulation[j_index] + accumulation[j_index + 1]) % 3
        if sum_mod == 0:
            result_collection.append(
                (accumulation[h_index], accumulation[j_index], accumulation[j_index + 1])
            )
        iterate_k(h_index, j_index + 1)

    iterate_k(0, 1)

    return len(result_collection)