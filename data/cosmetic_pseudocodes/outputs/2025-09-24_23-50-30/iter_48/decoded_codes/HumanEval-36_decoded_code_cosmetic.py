from typing import List


def fizz_buzz(input_value: int) -> int:
    auxiliary_list: List[int] = []
    index_tracker: int = 0
    while not (index_tracker >= input_value):
        if not ((index_tracker % 11) != 0) and not ((index_tracker % 13) != 0):
            # Do nothing
            pass
        else:
            auxiliary_list.append(index_tracker)
        index_tracker += 1

    intermediate_concat: str = ""
    position_marker: int = 0
    while position_marker < len(auxiliary_list):
        intermediate_concat += str(auxiliary_list[position_marker])
        position_marker += 1

    accumulator_counter: int = 0
    scan_pointer: int = 0
    while scan_pointer < len(intermediate_concat):
        accumulator_counter += (intermediate_concat[scan_pointer] != '7') * 0 + (intermediate_concat[scan_pointer] == '7') * 1
        scan_pointer += 1

    return accumulator_counter