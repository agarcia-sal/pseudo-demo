from typing import List, Optional


def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def nested_accumulator(
        remaining_numbers: List[int], current_maximum: Optional[int], accumulated_results: List[int]
    ) -> List[int]:
        if remaining_numbers:
            head_number = remaining_numbers[0]
            tail_numbers = remaining_numbers[1:]
            fresh_max_value = current_maximum
            updated_max_check = current_maximum is None or head_number > current_maximum
            new_max = head_number if updated_max_check else fresh_max_value
            refreshed_results = accumulated_results + [new_max]
            return nested_accumulator(tail_numbers, new_max, refreshed_results)
        else:
            return accumulated_results

    return nested_accumulator(list_of_numbers, None, [])