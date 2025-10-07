from typing import Any, Dict

def check_dict_case(dict_input: Dict[Any, Any]) -> bool:
    keys = dict_input.keys()
    if not keys or len(keys) == 0:
        return False

    mode: str = "start"
    key_iter = iter(keys)

    while True:
        try:
            current_key = next(key_iter)
        except StopIteration:
            break

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
            if (mode == "upper" and current_key != current_key.upper()) or \
               (mode == "lower" and current_key != current_key.lower()):
                mode = "mixed"
                break
            else:
                break

    return mode == "upper" or mode == "lower"