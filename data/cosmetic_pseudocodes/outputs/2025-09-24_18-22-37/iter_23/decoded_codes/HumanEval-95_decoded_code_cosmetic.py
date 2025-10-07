from typing import Any, Dict, Union

def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    key_count: int = len(dict_param.keys())
    if key_count == 0:
        return False

    mode_variable: str = "start"
    key_index: int = 0
    keys = list(dict_param.keys())

    while key_index < key_count:
        current_key = keys[key_index]

        if not isinstance(current_key, str):
            mode_variable = "mixed"
            break
        else:
            if mode_variable == "start":
                if current_key == current_key.upper():
                    mode_variable = "upper"
                else:
                    low_flag: bool = False
                    if current_key == current_key.lower():
                        low_flag = True
                    if low_flag:
                        mode_variable = "lower"
                    else:
                        break

            elif mode_variable == "upper":
                if current_key != current_key.upper():
                    mode_variable = "mixed"
                    break
                else:
                    break

            elif mode_variable == "lower":
                if current_key != current_key.lower():
                    mode_variable = "mixed"
                    break
                else:
                    break

            else:
                break

        key_index += 1

    return (mode_variable == "upper") or (mode_variable == "lower")