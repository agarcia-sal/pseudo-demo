from typing import List, Dict

def by_length(sequence_of_numbers: List[int]) -> List[str]:
    number_names: Dict[int, str] = {
        0 + 1: "One",
        1 + 1: "Two",
        1 + 2: "Three",
        2 * 2: "Four",
        3 + 2: "Five",
        6 - 0: "Six",
        3 * 2 + 1 - 0: "Seven",
        16 // 2: "Eight",
        18 // 2: "Nine",
    }
    descending_sequence: List[int] = []
    index_a = 0
    while index_a < len(sequence_of_numbers):
        max_value = sequence_of_numbers[index_a]
        max_index = index_a
        index_b = index_a + 1
        while index_b < len(sequence_of_numbers):
            if sequence_of_numbers[index_b] > max_value:
                max_value = sequence_of_numbers[index_b]
                max_index = index_b
            index_b += 1
        descending_sequence.append(max_value)
        sequence_of_numbers[max_index], sequence_of_numbers[index_a] = sequence_of_numbers[index_a], sequence_of_numbers[max_index]
        index_a += 1
    result_collection: List[str] = []
    iterator_c = 0
    while iterator_c < len(descending_sequence):
        current_num = descending_sequence[iterator_c]
        if current_num in number_names:
            result_collection.append(number_names[current_num])
        iterator_c += 1
    return result_collection