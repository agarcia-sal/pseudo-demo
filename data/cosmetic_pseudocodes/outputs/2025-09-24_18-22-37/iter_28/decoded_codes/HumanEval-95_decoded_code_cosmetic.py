from typing import Any, Dict


def check_dict_case(dict_obj: Dict[Any, Any]) -> bool:
    if len(dict_obj) == 0:
        return False

    mode_state: str = "start"
    key_list = list(dict_obj.keys())
    iter_index = 0

    while iter_index < len(key_list):
        current_key = key_list[iter_index]

        if not isinstance(current_key, str):
            mode_state = "mixed"
            break

        if mode_state == "start":
            if current_key == current_key.upper():
                mode_state = "upper"
            elif current_key == current_key.lower():
                mode_state = "lower"
            else:
                break
        elif (mode_state == "upper" and current_key != current_key.upper()) or (
            mode_state == "lower" and current_key != current_key.lower()
        ):
            mode_state = "mixed"
            break
        else:
            break

        iter_index += 1

    return mode_state == "upper" or mode_state == "lower"