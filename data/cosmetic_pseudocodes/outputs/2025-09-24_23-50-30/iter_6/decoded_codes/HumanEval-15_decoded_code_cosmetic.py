from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    counter: int = 0
    while counter < integer_n + 1:
        result_list.append("" + str(counter))
        counter += 1
    final_string: str = result_list[0]
    index_tracker: int = 1
    while index_tracker < len(result_list):
        final_string += " " + result_list[index_tracker]
        index_tracker += 1
    return final_string