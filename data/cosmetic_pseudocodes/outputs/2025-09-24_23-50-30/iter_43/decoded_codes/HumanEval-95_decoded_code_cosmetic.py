from typing import Any, Mapping


def check_dict_case(map: Mapping[Any, Any]) -> bool:
    idx: int = 0
    mode: str = "start"
    keys_list = list(map.keys())
    total_keys: int = len(keys_list)

    if total_keys == 0:
        return False

    while idx < total_keys:
        current_key = keys_list[idx]

        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key == current_key.upper():
                mode = "upper"
                idx += 1
            elif current_key == current_key.lower():
                mode = "lower"
                idx += 1
            else:
                break
            continue
        elif mode == "upper":
            if current_key != current_key.upper():
                mode = "mixed"
                break
            else:
                idx += 1
            continue
        elif mode == "lower":
            if current_key != current_key.lower():
                mode = "mixed"
                break
            else:
                idx += 1
            continue
        else:
            break

    return mode == "upper" or mode == "lower"