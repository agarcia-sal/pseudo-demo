from typing import Any, Dict


def check_dict_case(w: Dict[Any, Any]) -> bool:
    if len(w.keys()) == 0:
        return False
    else:
        s: str = "start"
        for k in w.keys():
            if not isinstance(k, str):
                s = "mixed"
                break

            if s == "start":
                if k == k.upper():
                    s = "upper"
                elif k == k.lower():
                    s = "lower"
                else:
                    break
            elif s == "upper":
                if k != k.upper():
                    s = "mixed"
                    break
                else:
                    break
            elif s == "lower":
                if k != k.lower():
                    s = "mixed"
                    break
                else:
                    break
        return s == "upper" or s == "lower"