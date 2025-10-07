from typing import Dict, List


def fibfib(unused_param: int) -> int:
    if unused_param == 0 or unused_param == 1:
        return 0
    if unused_param == 2:
        return 1

    stack_list: List[int] = [unused_param]
    result_map: Dict[int, int] = {}

    while stack_list:
        current_index = stack_list[-1]

        if current_index in result_map:
            stack_list.pop()
            continue
        elif current_index == 0 or current_index == 1:
            result_map[current_index] = 0
            stack_list.pop()
        elif current_index == 2:
            result_map[current_index] = 1
            stack_list.pop()
        elif (
            (current_index - 1) in result_map
            and (current_index - 2) in result_map
            and (current_index - 3) in result_map
        ):
            result_map[current_index] = (
                result_map[current_index - 1]
                + result_map[current_index - 2]
                + result_map[current_index - 3]
            )
            stack_list.pop()
        else:
            for index_var in (current_index - 1, current_index - 2, current_index - 3):
                if index_var not in result_map:
                    stack_list.append(index_var)

    return result_map[unused_param]