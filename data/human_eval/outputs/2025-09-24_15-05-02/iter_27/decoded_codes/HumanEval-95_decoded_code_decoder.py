from typing import Dict, Any


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if not dictionary:
        return False

    state: str = "start"
    for key in dictionary.keys():
        if not isinstance(key, str):
            state = "mixed"
            break

        if state == "start":
            if key.isupper():
                state = "upper"
            elif key.islower():
                state = "lower"
            else:
                # key is a string but neither all upper nor all lower
                break
        elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
            state = "mixed"
            break
        else:
            break

    return state == "upper" or state == "lower"