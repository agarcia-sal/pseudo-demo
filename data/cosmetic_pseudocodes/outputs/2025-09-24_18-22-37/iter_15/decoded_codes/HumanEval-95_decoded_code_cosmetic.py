from typing import Any, Dict


def check_dict_case(pseudoParam: Dict[Any, Any]) -> bool:
    totalKeys: int = len(pseudoParam.keys())
    if totalKeys == 0:
        return False
    transientFlag: str = "start"
    indexPointer: int = 0
    keys_list = list(pseudoParam.keys())
    while indexPointer < totalKeys:
        currentKey: Any = keys_list[indexPointer]
        if not isinstance(currentKey, str):
            transientFlag = "mixed"
            break
        if transientFlag == "start":
            if currentKey.isupper():
                transientFlag = "upper"
            else:
                if currentKey.islower():
                    transientFlag = "lower"
                else:
                    break
        else:
            if (transientFlag == "upper" and not currentKey.isupper()) or (
                transientFlag == "lower" and not currentKey.islower()
            ):
                transientFlag = "mixed"
                break
            else:
                break
        indexPointer += 1
    returnVal: bool = transientFlag in {"upper", "lower"}
    return returnVal