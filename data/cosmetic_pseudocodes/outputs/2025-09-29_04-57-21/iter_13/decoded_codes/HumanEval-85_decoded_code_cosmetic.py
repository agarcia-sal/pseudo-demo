from typing import List

def add(list_of_integers: List[int]) -> int:
    def accumulate_even_at_odd_indices(current_index: int, collected_sum: int) -> int:
        if current_index >= len(list_of_integers):
            return collected_sum
        updated_sum = collected_sum + list_of_integers[current_index] if list_of_integers[current_index] % 2 == 0 else collected_sum
        return accumulate_even_at_odd_indices(current_index + 2, updated_sum)

    return accumulate_even_at_odd_indices(1, 0)