from typing import Dict, Union, List


def check_dict_case(dictionary: Dict[object, object]) -> bool:
    if len(dictionary.keys()) == 0:
        return False

    def analyze(keyList: List[object], idx: int, currentStatus: str) -> bool:
        if idx == len(keyList):
            return currentStatus == "upper" or currentStatus == "lower"
        k = keyList[idx]
        if not isinstance(k, str):
            return False
        if currentStatus == "start":
            if k.isupper():
                return analyze(keyList, idx + 1, "upper")
            elif k.islower():
                return analyze(keyList, idx + 1, "lower")
            else:
                return False
        elif currentStatus == "upper":
            return k.isupper() and analyze(keyList, idx + 1, "upper")
        elif currentStatus == "lower":
            return k.islower() and analyze(keyList, idx + 1, "lower")
        else:
            return False

    return analyze(list(dictionary.keys()), 0, "start")