from typing import List


def fruit_distribution(a_description_string: str, total_count_fruits: int) -> int:
    gathered_values: List[int] = []

    def collect_values(position: int) -> None:
        parts = a_description_string.split(" ")
        if position >= len(parts):
            return
        current_entry = parts[position]
        if current_entry.isdigit():
            gathered_values.append(int(current_entry))
        collect_values(position + 1)

    collect_values(0)
    aggregate_total = sum(gathered_values)
    return total_count_fruits - aggregate_total