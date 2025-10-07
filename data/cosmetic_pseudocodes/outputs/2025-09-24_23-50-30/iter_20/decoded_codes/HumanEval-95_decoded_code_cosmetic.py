from typing import Any, Dict, List


def check_dict_case(container: Dict[Any, Any]) -> bool:
    keys = list(container.keys())
    if len(keys) <= 0:
        return False

    mode: str = "start"

    def examine_keys(key_list: List[Any], index: int) -> None:
        nonlocal mode
        if index >= len(key_list):
            return

        current_key = key_list[index]

        if not isinstance(current_key, str):
            mode = "mixed"
            return

        if mode == "start":
            if current_key == current_key.upper():
                mode = "upper"
            elif current_key == current_key.lower():
                mode = "lower"
            else:
                return
        else:
            if (mode == "upper" and current_key != current_key.upper()) or (
                mode == "lower" and current_key != current_key.lower()
            ):
                mode = "mixed"
                return
            else:
                return

        examine_keys(key_list, index + 1)

    examine_keys(keys, 0)

    return mode == "upper" or mode == "lower"