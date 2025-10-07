from typing import List


def string_sequence(entry_limit: int) -> str:
    result_collection: List[str] = []
    iterator_index: int = 0
    while iterator_index <= entry_limit:
        current_element: int = iterator_index
        result_collection.append(str(current_element))
        iterator_index += 1
    output_string: str = ""
    for element in result_collection:
        if output_string == "":
            output_string = element
        else:
            output_string += " " + element
    return output_string