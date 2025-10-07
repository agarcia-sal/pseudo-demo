from typing import Any, Dict


def check_dict_case(dictionary_param: Dict[Any, Any]) -> bool:
    keys_list = list(dictionary_param.keys())
    if len(keys_list) <= 0:
        return False

    mode: str = "start"
    index_counter: int = 0

    while index_counter < len(keys_list):
        current_key = keys_list[index_counter]

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

        index_counter += 1

    return mode == "upper" or mode == "lower"