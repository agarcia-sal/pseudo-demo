from typing import List

def intersperse(sequence_of_ints: List[int], separator: int) -> List[int]:
    if not sequence_of_ints:
        return []

    assembled_list: List[int] = []
    index_counter = 0
    while index_counter < len(sequence_of_ints) - 1:
        assembled_list.append(sequence_of_ints[index_counter])
        assembled_list.append(separator)
        index_counter += 1

    assembled_list.append(sequence_of_ints[-1])

    return assembled_list