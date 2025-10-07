from typing import Any, Dict


def check_dict_case(alphabet: Dict[Any, Any]) -> bool:
    keys_list = list(alphabet.keys())
    resultQ = len(keys_list)
    if resultQ == 0:
        return False

    statusZ: str = "start"
    indxP: int = 0
    keyX: Any = None

    while indxP < resultQ:
        keyX = keys_list[indxP]
        if not isinstance(keyX, str):
            statusZ = "mixed"
            break

        if statusZ == "start":
            if keyX == keyX.upper():
                statusZ = "upper"
            else:
                if keyX == keyX.lower():
                    statusZ = "lower"
                else:
                    break
        else:
            upperCheck = (statusZ == "upper" and not (keyX == keyX.upper()))
            lowerCheck = (statusZ == "lower" and not (keyX == keyX.lower()))
            if upperCheck or lowerCheck:
                statusZ = "mixed"
                break
            else:
                break
        indxP += 1

    return statusZ == "upper" or statusZ == "lower"