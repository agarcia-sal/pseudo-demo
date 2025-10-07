from typing import List


def string_sequence(parameter_m: int) -> str:
    result_list: List[str] = []
    iterator_index: int = 0
    while iterator_index <= parameter_m:
        result_list.append(str(iterator_index))
        iterator_index += 1

    assembled_string: str = ""
    index_tracker: int = 0
    if len(result_list) == 0:
        assembled_string = ""
    else:
        assembled_string = result_list[0]
        index_tracker = 1
        while not (index_tracker > len(result_list) - 1):
            assembled_string += " " + result_list[index_tracker]
            index_tracker += 1

    return assembled_string