from typing import Any, Mapping


def check_dict_case(mapping: Mapping[Any, Any]) -> bool:
    keys = list(mapping.keys())
    if len(keys) == 0:
        return False

    def loop(keys: list[Any], index: int, mode: str) -> bool:
        if index >= len(keys):
            return mode == "upper" or mode == "lower"
        current_key = keys[index]
        if not isinstance(current_key, str):
            return False
        if mode == "start":
            if current_key == current_key.upper():
                return loop(keys, index + 1, "upper")
            elif current_key == current_key.lower():
                return loop(keys, index + 1, "lower")
            else:
                return False
        elif (mode == "upper" and current_key != current_key.upper()) or (mode == "lower" and current_key != current_key.lower()):
            return False
        else:
            return loop(keys, index + 1, mode)

    return loop(keys, 0, "start")