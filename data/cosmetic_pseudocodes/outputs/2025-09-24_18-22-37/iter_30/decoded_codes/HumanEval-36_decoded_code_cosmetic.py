from typing import List


def fizz_buzz(number_limit: int) -> int:
    result_sequence: List[int] = []
    index_var: int = 0
    while index_var < number_limit:
        remainder_eleven = index_var % 11
        remainder_thirteen = index_var % 13
        include_element = (remainder_eleven == 0) or (remainder_thirteen == 0)
        if include_element:
            result_sequence.append(index_var)
        index_var += 1

    combined_text: str = ""
    iter_var: int = 0
    while iter_var < len(result_sequence):
        item = result_sequence[iter_var]
        combined_text += str(item)
        iter_var += 1

    counter_seven: int = 0
    position: int = 0
    while position < len(combined_text):
        current_char = combined_text[position]
        if current_char == '7':
            counter_seven += 1
        position += 1

    return counter_seven