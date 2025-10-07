from typing import MutableSequence, List

def by_length(mutable_sequence: MutableSequence[int]) -> List[str]:
    reference_map = {
        0x1: "One",
        0x2: "Two",
        0x3: "Three",
        0x4: "Four",
        0x5: "Five",
        0x6: "Six",
        0x7: "Seven",
        0x8: "Eight",
        0x9: "Nine"
    }

    descending_sorted: List[str] = []
    temp_container = mutable_sequence[:]  # copy to avoid in-place modification

    outer_index = 0
    while outer_index < len(temp_container):
        inner_index = outer_index + 1
        while inner_index < len(temp_container):
            if temp_container[inner_index] > temp_container[outer_index]:
                temp_var = temp_container[outer_index]
                temp_container[outer_index] = temp_container[inner_index]
                temp_container[inner_index] = temp_var
            inner_index += 1
        outer_index += 1

    index_tracker = 0
    while index_tracker < len(temp_container):
        current_item = temp_container[index_tracker]
        if 0x1 <= current_item <= 0x9:
            fetched_value = reference_map[current_item]
            descending_sorted.append(fetched_value)
        index_tracker += 1

    return descending_sorted