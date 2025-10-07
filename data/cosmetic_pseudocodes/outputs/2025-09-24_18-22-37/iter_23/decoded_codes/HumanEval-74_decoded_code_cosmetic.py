from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    size_counter: int = 0
    index_x: int = 0
    while index_x < len(list_one):
        current_piece = list_one[index_x]
        piece_length = len(current_piece)
        size_counter += piece_length
        index_x += 1

    size_metric: int = 0
    cursor_y: int = 0
    while cursor_y < len(list_two):
        item_element = list_two[cursor_y]
        elem_length = len(item_element)
        size_metric += elem_length
        cursor_y += 1

    if size_counter <= size_metric:
        return list_one
    else:
        return list_two