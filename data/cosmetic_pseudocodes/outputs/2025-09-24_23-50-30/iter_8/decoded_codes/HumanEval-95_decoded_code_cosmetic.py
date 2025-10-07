from typing import Any, Dict

def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary.keys()) == 0:
        return False

    mode: str = "start"
    keys = list(dictionary.keys())
    index = 0

    while index < len(keys):
        currentKey = keys[index]

        if not isinstance(currentKey, str):
            mode = "mixed"
            break

        if mode == "start":
            if currentKey.isupper():
                mode = "upper"
            else:
                if currentKey.islower():
                    mode = "lower"
                else:
                    break
        else:
            if (mode == "upper" and not currentKey.isupper()) or (mode == "lower" and not currentKey.islower()):
                mode = "mixed"
                break
            else:
                break

        index += 1

    return mode == "upper" or mode == "lower"