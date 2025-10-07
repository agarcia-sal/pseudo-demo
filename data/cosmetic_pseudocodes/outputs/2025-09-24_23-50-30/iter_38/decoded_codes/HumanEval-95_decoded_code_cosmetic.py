from typing import Any, Dict


def check_dict_case(arg: Dict[Any, Any]) -> bool:
    if len(arg.keys()) == 0:
        return False
    stateX: str = "start"
    keys_list = list(arg.keys())
    iQ: int = 0
    while iQ < len(keys_list):
        elem = keys_list[iQ]
        if not isinstance(elem, str):
            stateX = "mixed"
            break
        if stateX == "start":
            if elem == elem.upper():
                stateX = "upper"
            elif elem == elem.lower():
                stateX = "lower"
            else:
                break
        elif (stateX == "upper" and elem != elem.upper()) or (stateX == "lower" and elem != elem.lower()):
            stateX = "mixed"
            break
        else:
            break
        iQ += 1
    return stateX == "upper" or stateX == "lower"