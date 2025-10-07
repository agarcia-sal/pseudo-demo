from typing import Mapping, Any

def check_dict_case(input_map: Mapping[Any, Any]) -> bool:
    if len(input_map) == 0:
        return False
    mode: str = "start"
    for element in input_map.keys():
        if not isinstance(element, str):
            mode = "mixed"
            break
        if mode == "start":
            if element == element.upper():
                mode = "upper"
            elif element == element.lower():
                mode = "lower"
            else:
                break
        else:
            if (mode == "upper" and element != element.upper()) or (mode == "lower" and element != element.lower()):
                mode = "mixed"
                break
            else:
                break
    return mode == "upper" or mode == "lower"