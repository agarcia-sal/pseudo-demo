from typing import List

def string_sequence(integer_n: int) -> str:
    list_of_strings: List[str] = []
    counter: int = 0

    while counter <= integer_n:
        current_string: str = str(counter)
        list_of_strings.append(current_string)
        counter += 1

    result_string: str = ""
    first_element: bool = True

    for element in list_of_strings:
        if first_element:
            result_string = element
            first_element = False
        else:
            result_string += " " + element

    return result_string