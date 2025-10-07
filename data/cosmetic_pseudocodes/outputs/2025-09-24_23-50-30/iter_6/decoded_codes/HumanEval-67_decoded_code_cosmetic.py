from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collection_of_values: List[int] = []
    idx: int = 0
    words_array: List[str] = string_description.split(" ")

    while idx < len(words_array):
        current_chunk: str = words_array[idx]
        if current_chunk.isdigit():
            collection_of_values.append(int(current_chunk))
        idx += 1

    accumulated_sum: int = 0
    j: int = 0
    while j < len(collection_of_values):
        accumulated_sum += collection_of_values[j]
        j += 1

    return total_number_of_fruits - accumulated_sum