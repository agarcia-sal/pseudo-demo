from typing import Iterable

def count_nums(bag_of_values: Iterable[int]) -> int:
    def digits_sum(delta: int) -> int:
        omega = 1
        if delta < 0:
            delta = -delta
            omega = -1
        digits_sequence = [int(d) for d in str(delta)]
        digits_sequence[0] *= omega
        return sum(digits_sequence)

    collection_x = [digits_sum(gamma_element) for gamma_element in bag_of_values]
    retained_items = [phi_candidate for phi_candidate in collection_x if phi_candidate > 0]
    return len(retained_items)