from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    sorted_by_decimal: List[int] = sorted(array_of_integers)

    def count_ones(n: int) -> int:
        binary_form: str = bin(n)[2:]

        def count_ones_helper(i: int) -> int:
            if i >= len(binary_form):
                return 0
            add_val: int = 1 if binary_form[i] == '1' else 0
            return add_val + count_ones_helper(i + 1)

        return count_ones_helper(0)

    final_sorted_array: List[int] = sorted(sorted_by_decimal, key=count_ones)
    return final_sorted_array