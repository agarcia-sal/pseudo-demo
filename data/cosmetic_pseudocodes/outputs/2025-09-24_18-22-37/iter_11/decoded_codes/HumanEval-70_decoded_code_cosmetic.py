from typing import List


def strange_sort_list(sequence_of_numbers: List[int]) -> List[int]:
    result_collection: List[int] = []
    toggle_indicator: bool = True

    while True:
        if not sequence_of_numbers:
            break

        extracted_value: int = 0

        if toggle_indicator:
            index_min: int = 0
            current_min: int = sequence_of_numbers[0]
            iterator_idx: int = 1
            while iterator_idx < len(sequence_of_numbers):
                compare_candidate: int = sequence_of_numbers[iterator_idx]
                if compare_candidate < current_min:
                    current_min = compare_candidate
                    index_min = iterator_idx
                iterator_idx += 1
            extracted_value = current_min
            result_collection.append(extracted_value)
            sequence_of_numbers.pop(index_min)
        else:
            index_max: int = 0
            current_max: int = sequence_of_numbers[0]
            iterator_idx_2: int = 1
            while iterator_idx_2 < len(sequence_of_numbers):
                candidate_max: int = sequence_of_numbers[iterator_idx_2]
                if candidate_max > current_max:
                    current_max = candidate_max
                    index_max = iterator_idx_2
                iterator_idx_2 += 1
            extracted_value = current_max
            result_collection.append(extracted_value)
            sequence_of_numbers.pop(index_max)

        toggle_indicator = not toggle_indicator

    return result_collection