from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    keys_list = list(dictionary.keys())
    if len(keys_list) == 0:
        return False

    state_flag = "start"
    index = 0

    while index < len(keys_list):
        current_key = keys_list[index]

        if not isinstance(current_key, str):
            state_flag = "mixed"
            break
        elif state_flag == "start":
            if current_key.upper() == current_key:
                state_flag = "upper"
            elif current_key.lower() == current_key:
                state_flag = "lower"
            else:
                break
        elif (state_flag == "upper" and current_key.upper() != current_key) or (
            state_flag == "lower" and current_key.lower() != current_key
        ):
            state_flag = "mixed"
            break
        else:
            break

        index += 1

    return state_flag == "upper" or state_flag == "lower"