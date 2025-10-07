from typing import Mapping, Any

def check_dict_case(input_map: Mapping[Any, Any]) -> bool:
    if len(input_map) == 0:
        return False

    marker: str = "start"
    keys = list(input_map.keys())
    index: int = 0
    length: int = len(keys)

    while index < length:
        item = keys[index]
        if not isinstance(item, str):
            marker = "mixed"
            break

        if marker == "start":
            isAllUpper = True
            isAllLower = True
            for ch in item:
                isUpperChar = "A" <= ch <= "Z"
                isLowerChar = "a" <= ch <= "z"
                if not isUpperChar:
                    isAllUpper = False
                if not isLowerChar:
                    isAllLower = False
            if isAllUpper:
                marker = "upper"
            elif isAllLower:
                marker = "lower"
            else:
                break

        else:
            if marker == "upper":
                validUpper = True
                for ch2 in item:
                    if not ("A" <= ch2 <= "Z"):
                        validUpper = False
                        break
                if not validUpper:
                    marker = "mixed"
                    break

            elif marker == "lower":
                validLower = True
                for ch3 in item:
                    if not ("a" <= ch3 <= "z"):
                        validLower = False
                        break
                if not validLower:
                    marker = "mixed"
                    break

            else:
                break

        index += 1

    result = marker in {"upper", "lower"}
    return result