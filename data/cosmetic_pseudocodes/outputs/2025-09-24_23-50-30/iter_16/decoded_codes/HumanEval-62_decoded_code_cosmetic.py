from typing import List, Tuple, Iterable


def derivative(list_of_coefficients: List[int]) -> List[int]:
    def multiply_index(
        accumulated_list: List[int], pair_with_index: Iterable[Tuple[int, int]]
    ) -> List[int]:
        pair_iter = iter(pair_with_index)
        try:
            coeff_value, coeff_index = next(pair_iter)
        except StopIteration:
            return accumulated_list
        return multiply_index(accumulated_list + [coeff_value * coeff_index], pair_iter)

    indexed_pairs: Iterable[Tuple[int, int]] = zip(list_of_coefficients, range(len(list_of_coefficients)))
    filtered_pairs = filter(lambda p: p[1] != 0, indexed_pairs)
    return multiply_index([], filtered_pairs)