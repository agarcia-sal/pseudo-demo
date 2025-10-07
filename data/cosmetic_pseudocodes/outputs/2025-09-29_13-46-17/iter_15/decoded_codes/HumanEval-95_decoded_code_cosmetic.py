from typing import Any, Mapping


def check_dict_case(dictionary: Mapping[Any, Any]) -> bool:
    keys = list(dictionary.keys())
    if not (0 < len(keys)):
        return False

    case_state = "start"

    def check_case(key: Any) -> str:
        nonlocal case_state
        if not isinstance(key, str):
            return "mixed"
        if case_state == "start":
            if key == key.upper():
                return "upper"
            elif key == key.lower():
                return "lower"
            else:
                return "fail"
        elif case_state == "upper" and key != key.upper():
            return "mixed"
        elif case_state == "lower" and key != key.lower():
            return "mixed"
        else:
            return "fail"

    def recurse(pos: int) -> str:
        nonlocal case_state
        if pos == 0:
            return case_state
        result = check_case(keys[len(keys) - pos])
        if result == "fail":
            return case_state
        elif result == "mixed":
            return "mixed"
        else:
            case_state = result
            return recurse(pos - 1)

    case_state = recurse(len(keys))
    return case_state == "upper" or case_state == "lower"