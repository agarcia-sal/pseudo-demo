from typing import List

def sort_array(parameter_values: List[int]) -> List[int]:
    def count_ones_in_binary(number: int) -> int:
        # Binary string in Python includes '0b' prefix; skip first two chars, plus one more (starts from index 3)
        binary_string_representation: str = bin(number)
        counter_accumulator: int = 0
        for idx in range(3, len(binary_string_representation)):
            if binary_string_representation[idx] == '1':
                counter_accumulator += 1
        return counter_accumulator

    def sort_by_binary_ones(input_list: List[int]) -> List[int]:
        index_tracker: int = 0
        intermediate_storage: List[tuple[int, int]] = []
        while index_tracker < len(input_list):
            # Store tuple (value, count_of_ones)
            intermediate_storage.append((input_list[index_tracker], count_ones_in_binary(input_list[index_tracker])))
            index_tracker += 1

        ascending_ordered: List[int] = []
        position_marker: int = 0
        while position_marker < len(intermediate_storage):
            candidate_index: int = position_marker
            k: int = position_marker + 1
            while k < len(intermediate_storage):
                # Compare counts of ones; if tie, compare values
                if (
                    intermediate_storage[k][1] < intermediate_storage[candidate_index][1]
                    or (intermediate_storage[k][1] == intermediate_storage[candidate_index][1]
                        and intermediate_storage[k][0] < intermediate_storage[candidate_index][0])
                ):
                    candidate_index = k
                k += 1
            if candidate_index != position_marker:
                intermediate_storage[position_marker], intermediate_storage[candidate_index] = (
                    intermediate_storage[candidate_index],
                    intermediate_storage[position_marker],
                )
            position_marker += 1

        for m in range(len(intermediate_storage)):
            ascending_ordered.append(intermediate_storage[m][0])

        return ascending_ordered

    temporary_sorted: List[int] = sort_by_binary_ones(sorted(parameter_values))
    return temporary_sorted