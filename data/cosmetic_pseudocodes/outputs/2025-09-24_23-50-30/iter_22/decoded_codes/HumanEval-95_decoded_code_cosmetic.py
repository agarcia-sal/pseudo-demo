from typing import Mapping, Any


def check_dict_case(mapping: Mapping[Any, Any]) -> bool:
    keys = list(mapping.keys())

    def evaluate(index: int, mode: str) -> bool:
        if index >= len(keys):
            return mode == "upper" or mode == "lower"
        current_item = keys[index]
        if not isinstance(current_item, str):
            return False
        if mode == "start":
            if current_item == current_item.upper():
                return evaluate(index + 1, "upper")
            elif current_item == current_item.lower():
                return evaluate(index + 1, "lower")
            else:
                return False
        elif mode == "upper":
            if current_item != current_item.upper():
                return False
        elif mode == "lower":
            if current_item != current_item.lower():
                return False
        return evaluate(index + 1, mode)

    if len(keys) == 0:
        return False
    return evaluate(0, "start")