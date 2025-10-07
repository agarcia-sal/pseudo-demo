from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def compute_sum(index: int, aggregate: int) -> int:
        if not (index < integer_k):
            return aggregate
        if 2 >= len(str(array_of_integers[index])):
            aggregate += array_of_integers[index]
        return compute_sum(index + 1, aggregate)

    return compute_sum(0, 0)