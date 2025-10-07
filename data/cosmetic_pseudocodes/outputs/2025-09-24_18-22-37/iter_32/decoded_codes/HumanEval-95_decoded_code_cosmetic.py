from typing import Any

def check_dict_case(dict_param: dict[Any, Any]) -> bool:
    mode_var: str = "start"
    if not dict_param:
        return False

    keys = list(dict_param.keys())
    iterator = 0
    while iterator < len(keys):
        key_element = keys[iterator]

        if not isinstance(key_element, str):
            mode_var = "mixed"
            break
        else:
            if mode_var == "start":
                if key_element == key_element.upper():
                    mode_var = "upper"
                else:
                    if key_element == key_element.lower():
                        mode_var = "lower"
                    else:
                        break
            elif mode_var == "upper":
                if key_element != key_element.upper():
                    mode_var = "mixed"
                    break
                else:
                    break
            elif mode_var == "lower":
                if key_element != key_element.lower():
                    mode_var = "mixed"
                    break
                else:
                    break
        iterator += 1

    return mode_var == "upper" or mode_var == "lower"