from typing import Any, Mapping


def check_dict_case(map_structure: Mapping[Any, Any]) -> bool:
    if len(map_structure) == 0:
        return False

    mode: str = "start"
    idx: int = 0
    keys = list(map_structure.keys())
    while True:
        if idx >= len(keys):
            break
        current_element = keys[idx]

        if not isinstance(current_element, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_element.isupper():
                mode = "upper"
            elif current_element.islower():
                mode = "lower"
            else:
                break
        else:
            if (mode == "upper" and not current_element.isupper()) or (mode == "lower" and not current_element.islower()):
                mode = "mixed"
                break
            else:
                break
        idx += 1

    return mode == "upper" or mode == "lower"