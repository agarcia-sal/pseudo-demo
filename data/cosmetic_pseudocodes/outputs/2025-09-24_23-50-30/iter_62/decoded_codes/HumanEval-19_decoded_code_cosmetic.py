from typing import List


def sort_numbers(alphanumeric_string: str) -> str:
    numeral_dictionary: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    def extract_words(pos: int, acc: str) -> List[str]:
        if pos < len(alphanumeric_string):
            current_char = alphanumeric_string[pos]
            if current_char != ' ':
                return extract_words(pos + 1, acc + current_char)
            elif len(acc) > 0:
                return [acc] + extract_words(pos + 1, '')
            else:
                return extract_words(pos + 1, '')
        else:
            return [acc] if len(acc) > 0 else []

    fragmented_list: List[str] = extract_words(0, '')

    def compare_elements(x: str, y: str) -> int:
        if numeral_dictionary[x] < numeral_dictionary[y]:
            return -1
        if numeral_dictionary[x] > numeral_dictionary[y]:
            return 1
        return 0

    ordered_list: List[str] = fragmented_list
    index_counter = 0

    def insertion_sort(lst: List[str]) -> List[str]:
        nonlocal index_counter
        if index_counter >= len(lst) - 1:
            return lst
        key_element = lst[index_counter + 1]
        position = index_counter
        while position >= 0 and compare_elements(lst[position], key_element) > 0:
            lst[position + 1] = lst[position]
            position -= 1
        lst[position + 1] = key_element
        index_counter += 1
        return insertion_sort(lst)

    ordered_list = insertion_sort(ordered_list)

    def join_with_space(elements: List[str]) -> str:
        if len(elements) == 0:
            return ''
        if len(elements) == 1:
            return elements[0]
        return elements[0] + ' ' + join_with_space(elements[1:])

    return join_with_space(ordered_list)