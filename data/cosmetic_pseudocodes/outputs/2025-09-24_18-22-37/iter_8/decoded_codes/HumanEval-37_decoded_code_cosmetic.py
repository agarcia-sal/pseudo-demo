from typing import Sequence, List, TypeVar

T = TypeVar('T')


def sort_even(sequence_of_items: Sequence[T]) -> List[T]:
    collection_of_even_positions: List[T] = []
    index_counter = 0
    while index_counter < len(sequence_of_items):
        if index_counter % 2 == 0:
            collection_of_even_positions.append(sequence_of_items[index_counter])
        index_counter += 1

    collection_of_odd_positions: List[T] = []
    iterator_variable = 0
    while iterator_variable < len(sequence_of_items):
        if iterator_variable % 2 == 1:
            collection_of_odd_positions.append(sequence_of_items[iterator_variable])
        iterator_variable += 1

    collection_of_even_positions.sort()

    result_sequence: List[T] = []

    zipped_pairs: List[tuple[T, T]] = []
    position_marker = 0
    min_length = min(len(collection_of_even_positions), len(collection_of_odd_positions))
    while position_marker < min_length:
        even_element = collection_of_even_positions[position_marker]
        odd_element = collection_of_odd_positions[position_marker]
        zipped_pairs.append((even_element, odd_element))
        position_marker += 1

    iterator_index = 0
    while iterator_index < len(zipped_pairs):
        temporary_tuple = zipped_pairs[iterator_index]
        result_sequence.append(temporary_tuple[0])
        result_sequence.append(temporary_tuple[1])
        iterator_index += 1

    if len(collection_of_even_positions) - len(collection_of_odd_positions) > 0:
        result_sequence.append(collection_of_even_positions[-1])

    return result_sequence