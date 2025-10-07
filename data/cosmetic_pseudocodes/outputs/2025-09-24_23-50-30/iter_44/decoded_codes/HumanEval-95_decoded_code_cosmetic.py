from typing import Any, Dict


def check_dict_case(dict_var: Dict[Any, Any]) -> bool:
    if not dict_var:
        return False

    mode: str = "start"

    for element in dict_var.keys():
        if not isinstance(element, str):
            mode = "mixed"
            break
        else:
            if mode == "start":
                if element == element.upper():
                    mode = "upper"
                elif element == element.lower():
                    mode = "lower"
                else:
                    break
            elif (mode == "upper" and element != element.upper()) or (mode == "lower" and element != element.lower()):
                mode = "mixed"
                break
            else:
                break

    return mode == "upper" or mode == "lower"