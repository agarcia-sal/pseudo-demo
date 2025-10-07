from typing import Mapping, Any

def check_dict_case(container: Mapping[Any, Any]) -> bool:
    keys_list = list(container.keys())
    if len(keys_list) == 0:
        return False

    mode: str = "start"
    index: int = 0

    while index < len(keys_list):
        current_key = keys_list[index]

        if not isinstance(current_key, str):
            mode = "mixed"
            break
        elif mode == "start":
            if current_key == current_key.upper():
                mode = "upper"
            elif current_key == current_key.lower():
                mode = "lower"
            else:
                break
        elif (mode == "upper" and current_key != current_key.upper()) or (mode == "lower" and current_key != current_key.lower()):
            mode = "mixed"
            break
        else:
            break

        index += 1

    return mode == "upper" or mode == "lower"