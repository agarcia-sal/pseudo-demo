from typing import Any, Dict

def check_dict_case(mu: Dict[Any, Any]) -> bool:
    keys = list(mu.keys())

    def traverse(idx: int, sigma: str) -> bool:
        if idx >= len(keys):
            return sigma == "upper" or sigma == "lower"
        p = keys[idx]
        if not isinstance(p, str):
            return False
        if sigma == "start":
            if p == p.upper():
                return traverse(idx + 1, "upper")
            elif p == p.lower():
                return traverse(idx + 1, "lower")
            else:
                return False
        if sigma == "upper" and p != p.upper():
            return False
        if sigma == "lower" and p != p.lower():
            return False
        return traverse(idx + 1, sigma)

    if len(keys) == 0:
        return False
    return traverse(0, "start")