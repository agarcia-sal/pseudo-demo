from typing import Any, Dict

def check_dict_case(dict_input: Dict[Any, Any]) -> bool:
    if len(dict_input) == 0:
        return False

    mode_state: str = "start"
    idx_counter: int = 0
    key_list = list(dict_input.keys())

    while idx_counter < len(key_list):
        current_key = key_list[idx_counter]
        idx_counter += 1

        if not isinstance(current_key, str):
            mode_state = "mixed"
            break

        if mode_state == "start":
            if current_key == current_key.upper():
                mode_state = "upper"
            else:
                if current_key == current_key.lower():
                    mode_state = "lower"
                else:
                    break

        elif mode_state == "upper":
            if current_key != current_key.upper():
                mode_state = "mixed"
                break
            else:
                break

        elif mode_state == "lower":
            if current_key != current_key.lower():
                mode_state = "mixed"
                break
            else:
                break

    return mode_state == "upper" or mode_state == "lower"