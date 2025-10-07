from typing import Any, Mapping

def check_dict_case(map: Mapping[Any, Any]) -> bool:
    keys = list(map.keys())
    if len(keys) == 0:
        return False
    state = "start"
    index = 0
    while index < len(keys):
        item = keys[index]
        if not isinstance(item, str):
            state = "mixed"
            break
        if state == "start":
            if item == item.upper():
                state = "upper"
            elif item == item.lower():
                state = "lower"
            else:
                break
        elif (state == "upper" and item != item.upper()) or (state == "lower" and item != item.lower()):
            state = "mixed"
            break
        elif state != "upper" and state != "lower":
            break
        index += 1
    return state == "upper" or state == "lower"