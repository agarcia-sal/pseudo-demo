from typing import Any, Dict


def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    if len(dict_param) == 0:
        return False

    flag_state = "start"
    for element_key in dict_param.keys():
        if not isinstance(element_key, str):
            flag_state = "mixed"
            break

        if flag_state == "start":
            if element_key == element_key.upper():
                flag_state = "upper"
            elif element_key == element_key.lower():
                flag_state = "lower"
            else:
                break

        elif flag_state == "upper":
            if element_key != element_key.upper():
                flag_state = "mixed"
                break

        elif flag_state == "lower":
            if element_key != element_key.lower():
                flag_state = "mixed"
                break

    return flag_state == "upper" or flag_state == "lower"