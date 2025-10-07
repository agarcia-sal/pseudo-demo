from typing import List

def string_sequence(integer_n: int) -> str:
    index: int = 0
    string_list: List[str] = []
    while index <= integer_n:
        string_list.append(str(index))
        index += 1
    output_string: str = ""
    for element in string_list:
        if output_string == "":
            output_string = element
        else:
            output_string += " " + element
    return output_string