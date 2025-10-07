from typing import Dict, Any

def check_dict_case(alpha: Dict[Any, Any]) -> bool:
    keys = list(alpha.keys())
    if len(keys) == 0:
        return False
    flag: str = "start"
    j: int = 0
    while j < len(keys):
        r = keys[j]
        if not isinstance(r, str):
            flag = "mixed"
            break
        if flag == "start":
            if r.isupper():
                flag = "upper"
            elif r.islower():
                flag = "lower"
            else:
                break
        else:
            if (flag == "upper" and not r.isupper()) or (flag == "lower" and not r.islower()):
                flag = "mixed"
                break
            else:
                break
        j += 1
    return flag == "upper" or flag == "lower"