from typing import Dict, Any


def check_dict_case(p1: Dict[Any, Any]) -> bool:
    def recur(p2: Dict[Any, Any], p3: str) -> bool:
        keys = list(p2.keys())
        if len(keys) == 0:
            return p3 != "start"  # True if in upper/lower mode, else False
        if p3 == "start":
            p4 = keys[0]
            p5 = keys[1:]
            if not isinstance(p4, str):
                return False
            if p4 == p4.upper():
                p6 = "upper"
            elif p4 == p4.lower():
                p6 = "lower"
            else:
                return False
            # Construct dict with keys p5 from p2
            p2_next = {k: p2[k] for k in p5}
            return recur(p2_next, p6)
        elif p3 == "upper" or p3 == "lower":
            if len(keys) == 0:
                return True
            p7 = keys[0]
            p8 = keys[1:]
            if not isinstance(p7, str):
                return False
            if p3 == "upper":
                if p7 == p7.upper():
                    p2_next = {k: p2[k] for k in p8}
                    return recur(p2_next, p3)
                else:
                    return False
            else:
                if p7 == p7.lower():
                    p2_next = {k: p2[k] for k in p8}
                    return recur(p2_next, p3)
                else:
                    return False
        else:
            return False

    return recur(p1, "start")