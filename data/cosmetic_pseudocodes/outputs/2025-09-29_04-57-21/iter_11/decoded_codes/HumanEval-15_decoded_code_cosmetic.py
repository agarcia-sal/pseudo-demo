from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    counter: int = 0

    while counter <= integer_n:
        result_list.append("" + str(counter))
        counter += 1

    output_string: str = ""
    index: int = 0

    while index < len(result_list):
        output_string += result_list[index]
        if index != len(result_list) - 1:
            output_string += " "
        index += 1

    return output_string