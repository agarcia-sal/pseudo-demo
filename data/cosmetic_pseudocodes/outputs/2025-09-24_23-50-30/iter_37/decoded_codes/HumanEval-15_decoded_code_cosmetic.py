from typing import List

def string_sequence(integer_n: int) -> str:
    sequence_list: List[str] = []
    counter: int = 0
    while counter <= integer_n:
        sequence_list.append(str(counter))
        counter += 1
    result_string: str = ""
    for element in sequence_list:
        if result_string == "":
            result_string = element
        else:
            result_string += " " + element
    return result_string