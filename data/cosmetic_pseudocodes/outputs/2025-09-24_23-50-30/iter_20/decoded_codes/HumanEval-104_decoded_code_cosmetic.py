from typing import Iterable, List, Set, Union

def unique_digits(input_collection: Iterable[Union[int, str]]) -> List[Union[int, str]]:
    output_set: Set[Union[int, str]] = set()
    index_counter: int = 0
    input_list = list(input_collection)  # to support indexing and length

    while index_counter < len(input_list):
        current_value = input_list[index_counter]
        digit_collection = set(str(current_value))
        # Check if no digit in digit_collection is an even digit
        if not any((int(digit) % 2 == 0) for digit in digit_collection if digit.isdigit()):
            output_set.add(current_value)
        index_counter += 1

    output_list = sorted(output_set)
    return output_list