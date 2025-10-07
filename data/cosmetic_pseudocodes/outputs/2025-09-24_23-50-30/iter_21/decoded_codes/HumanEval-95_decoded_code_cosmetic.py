from typing import Any, Dict


def check_dict_case(dictionary_param: Dict[Any, Any]) -> bool:
    if len(dictionary_param.keys()) == 0:
        return False

    mode: str = "start"
    keys_list = list(dictionary_param.keys())
    index = 0

    while index < len(keys_list):
        current_key = keys_list[index]

        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key == current_key.upper():
                mode = "upper"
            elif current_key == current_key.lower():
                mode = "lower"
            else:
                break
        else:
            if (mode == "upper" and current_key != current_key.upper()) or (
                mode == "lower" and current_key != current_key.lower()
            ):
                mode = "mixed"
                break
            else:
                break

        index += 1

    return mode == "upper" or mode == "lower"