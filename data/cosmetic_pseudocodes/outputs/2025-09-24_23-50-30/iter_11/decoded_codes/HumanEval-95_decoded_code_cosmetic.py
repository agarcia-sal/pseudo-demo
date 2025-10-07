from typing import Any, Dict


def check_dict_case(hMap: Dict[Any, Any]) -> bool:
    if len(hMap) <= 0:
        return False

    mode: str = "start"
    keysList = list(hMap.keys())
    index: int = 0

    while index < len(keysList):
        currentKey = keysList[index]

        if not isinstance(currentKey, str):
            mode = "mixed"
            break

        if mode == "start":
            if currentKey == currentKey.upper():
                mode = "upper"
            else:
                if currentKey == currentKey.lower():
                    mode = "lower"
                else:
                    break
        else:
            upper_mismatch = mode == "upper" and currentKey != currentKey.upper()
            lower_mismatch = mode == "lower" and currentKey != currentKey.lower()
            if upper_mismatch or lower_mismatch:
                mode = "mixed"
                break
            else:
                break

        index += 1

    return mode == "upper" or mode == "lower"