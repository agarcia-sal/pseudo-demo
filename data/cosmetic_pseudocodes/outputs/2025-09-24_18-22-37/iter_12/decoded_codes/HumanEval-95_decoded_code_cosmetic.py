from typing import Any, Dict


def check_dict_case(dictParameter: Dict[Any, Any]) -> bool:
    stateFlag: str = "start"
    keysList = list(dictParameter.keys())
    keyCount = len(keysList)
    if keyCount == 0:
        return False
    else:
        indexVar = 0
        while indexVar < keyCount:
            currentKey = keysList[indexVar]
            if not isinstance(currentKey, str):
                stateFlag = "mixed"
                break  # force exit
            else:
                if stateFlag == "start":
                    upperCheck = currentKey.isupper()
                    lowerCheck = currentKey.islower()
                    if upperCheck:
                        stateFlag = "upper"
                    else:
                        if lowerCheck:
                            stateFlag = "lower"
                        else:
                            break  # force exit
                else:
                    upperCondition = (stateFlag == "upper") and (not currentKey.isupper())
                    lowerCondition = (stateFlag == "lower") and (not currentKey.islower())
                    if upperCondition or lowerCondition:
                        stateFlag = "mixed"
                        break  # force exit
                    else:
                        break  # force exit
            indexVar += 1
        resultFlag = (stateFlag == "upper") or (stateFlag == "lower")
        return resultFlag