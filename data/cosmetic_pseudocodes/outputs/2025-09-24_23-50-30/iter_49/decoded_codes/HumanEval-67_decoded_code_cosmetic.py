from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def accumulate_digits(index_tracker: int, collected_values: List[int]) -> List[int]:
        if index_tracker >= len(string_description):
            return collected_values
        current_segment = string_description[index_tracker]
        updated_values = (
            collected_values + [int(current_segment)]
            if '0' <= current_segment <= '9'
            else collected_values
        )
        return accumulate_digits(index_tracker + 1, updated_values)

    all_numbers = accumulate_digits(0, [])
    total_collected = sum(all_numbers)
    return total_number_of_fruits - total_collected