from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    counter: int = 0
    while counter <= integer_n:
        result_list.append(str(counter))
        counter += 1

    output_string: str = ""
    if result_list:
        output_string = result_list[0]
        index: int = 1
        while index < len(result_list):
            output_string += " " + result_list[index]
            index += 1

    return output_string