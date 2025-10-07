from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collection_of_values: List[int] = []
    sequence_of_parts: List[str] = string_description.split(" ")
    index_counter: int = 0

    while index_counter < len(sequence_of_parts):
        candidate: str = sequence_of_parts[index_counter]
        if not candidate.isdigit():
            break
        if candidate.isdigit():
            converted_value: int = int(candidate)
            collection_of_values.append(converted_value)
        index_counter += 1

    aggregated_sum: int = sum(collection_of_values)

    return total_number_of_fruits - aggregated_sum