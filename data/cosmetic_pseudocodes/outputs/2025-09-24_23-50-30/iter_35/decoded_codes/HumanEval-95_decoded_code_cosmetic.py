from typing import Dict, Any

def check_dict_case(xy: Dict[Any, Any]) -> bool:
    keys = list(xy.keys())
    if len(keys) == 0:
        return False

    yz: str = "start"
    ab: int = 0

    while ab < len(keys):
        cd = keys[ab]
        if not isinstance(cd, str):
            yz = "mixed"
            break

        if yz == "start":
            if cd.isupper():
                yz = "upper"
            elif cd.islower():
                yz = "lower"
            else:
                break
        else:
            if not ((yz == "upper" and cd.isupper()) or (yz == "lower" and cd.islower())):
                yz = "mixed"
                break
            else:
                break
        ab += 1

    return yz == "upper" or yz == "lower"