from typing import List


def string_sequence(input_value: int) -> str:
    collection_of_strings: List[str] = []
    current_counter: int = 0

    while current_counter <= input_value:
        number_as_string: str = str(current_counter)
        collection_of_strings.append(number_as_string)
        current_counter += 1

    result_string: str = ""

    if collection_of_strings:
        index_var: int = 0
        limit: int = len(collection_of_strings) - 1
        while index_var < limit:
            result_string += collection_of_strings[index_var] + " "
            index_var += 1
        result_string += collection_of_strings[limit]

    return result_string