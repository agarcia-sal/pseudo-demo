from typing import List

def string_sequence(integer_n: int) -> str:
    list_result: List[str] = []
    index_tracker: int = 0
    while index_tracker <= integer_n:
        list_result.append(str(index_tracker))
        index_tracker += 1
    output_string: str = ""
    flag_first: bool = True
    for element in list_result:
        if flag_first:
            output_string = element
            flag_first = False
        else:
            output_string += " " + element
    return output_string