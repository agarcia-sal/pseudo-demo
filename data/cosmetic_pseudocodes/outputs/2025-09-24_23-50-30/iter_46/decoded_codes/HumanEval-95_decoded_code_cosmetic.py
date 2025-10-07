from typing import Any, Dict

def check_dict_case(dict_obj: Dict[Any, Any]) -> bool:
    keys = list(dict_obj.keys())

    def iterate_keys(idx: int, curr_state: str) -> bool:
        if idx >= len(keys):
            return curr_state == "upper" or curr_state == "lower"

        k = keys[idx]

        if not isinstance(k, str):
            return False

        if curr_state == "start":
            if k.isupper():
                return iterate_keys(idx + 1, "upper")
            elif k.islower():
                return iterate_keys(idx + 1, "lower")
            else:
                return False
        elif curr_state == "upper":
            if not k.isupper():
                return False
            return iterate_keys(idx + 1, "upper")
        elif curr_state == "lower":
            if not k.islower():
                return False
            return iterate_keys(idx + 1, "lower")
        else:
            return False

    if len(keys) != 0:
        return iterate_keys(0, "start")
    else:
        return False