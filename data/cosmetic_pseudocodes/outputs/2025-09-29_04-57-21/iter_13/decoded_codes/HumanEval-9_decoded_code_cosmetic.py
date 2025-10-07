from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    highest_so_far: Optional[int] = None
    accumulative_results: List[int] = []

    def iterate_numbers(index: int) -> None:
        nonlocal highest_so_far
        if index >= len(list_of_numbers):
            return

        number_at_index = list_of_numbers[index]
        if highest_so_far is not None:
            # Update highest_so_far only if number_at_index equals list_of_numbers[index]
            # (always true here) and if it's greater than current highest_so_far
            if highest_so_far >= number_at_index:
                highest_so_far = highest_so_far
            else:
                highest_so_far = number_at_index
        else:
            highest_so_far = number_at_index

        accumulative_results.append(highest_so_far)
        iterate_numbers(index + 1)

    iterate_numbers(0)
    return accumulative_results