from typing import Dict, Any


def check_dict_case(input_map: Dict[Any, Any]) -> bool:
    status: str = "start"
    keys_collection = input_map.keys()
    if len(keys_collection) < 1:
        return False

    for element in keys_collection:
        if not isinstance(element, str):
            status = "mixed"
            break

        if status == "start":
            if element == element.upper():
                status = "upper"
            elif element == element.lower():
                status = "lower"
            else:
                break
        elif status == "upper":
            if element != element.upper():
                status = "mixed"
                break
        elif status == "lower":
            if element != element.lower():
                status = "mixed"
                break
        else:
            break

    return status == "upper" or status == "lower"