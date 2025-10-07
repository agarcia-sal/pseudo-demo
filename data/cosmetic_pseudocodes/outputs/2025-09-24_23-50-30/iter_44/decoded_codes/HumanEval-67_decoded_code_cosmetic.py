from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    fresh_idx = 0
    gathered_values: List[int] = []

    length = len(string_description)
    while fresh_idx < length:
        segment_start = fresh_idx
        while fresh_idx < length and string_description[fresh_idx] != ' ':
            fresh_idx += 1
        fragment = string_description[segment_start:fresh_idx]
        if fragment and all(c.isdigit() for c in fragment):
            gathered_values.append(int(fragment))
        fresh_idx += 1

    def recursive_sum(values: List[int], position: int) -> int:
        if position >= len(values):
            return 0
        else:
            return values[position] + recursive_sum(values, position + 1)

    return total_number_of_fruits - recursive_sum(gathered_values, 0)