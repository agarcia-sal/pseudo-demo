from typing import Any, Mapping


def check_dict_case(mapping: Mapping[Any, Any]) -> bool:
    keys_list = list(mapping.keys())
    total_keys = len(keys_list)
    if total_keys == 0:
        return False

    mode: str = "start"
    indexer = 0

    while indexer < total_keys:
        current_key = keys_list[indexer]
        indexer += 1

        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key.isupper():
                mode = "upper"
            else:
                if current_key.islower():
                    mode = "lower"
                else:
                    break
        else:
            is_upper_mode_error = (mode == "upper") and (not current_key.isupper())
            is_lower_mode_error = (mode == "lower") and (not current_key.islower())

            if is_upper_mode_error or is_lower_mode_error:
                mode = "mixed"
                break

    return mode == "upper" or mode == "lower"