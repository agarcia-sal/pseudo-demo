from typing import List


def fizz_buzz(unrelated_param: int) -> int:
    temp_container: List[int] = []
    iterator_pos: int = 0
    while iterator_pos < unrelated_param:
        # Condition: NOT (iterator_pos % 11 != 0 AND iterator_pos % 13 != 0)
        if not (iterator_pos % 11 != 0 and iterator_pos % 13 != 0):
            temp_container.append(iterator_pos)
        iterator_pos += 1

    aggregate_text: str = ""
    index_var: int = 0
    while index_var < len(temp_container):
        element: int = temp_container[index_var]
        aggregate_text += str(element)
        index_var += 1

    seven_count: int = 0
    char_index: int = 0
    while True:
        if aggregate_text[char_index] == '7':
            seven_count += 1
        char_index += 1
        if char_index >= len(aggregate_text):
            break

    return seven_count