from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    keys_list = list(dictionary.keys())
    if not keys_list:
        return False

    status: str = "start"

    def process_keys(idx: int) -> None:
        nonlocal status
        if idx >= len(keys_list):
            return

        currentKey = keys_list[idx]

        if not isinstance(currentKey, str):
            status = "mixed"
            return

        if status == "start":
            if currentKey == currentKey.upper():
                status = "upper"
            elif currentKey == currentKey.lower():
                status = "lower"
            else:
                return
        else:
            if (status == "upper" and currentKey != currentKey.upper()) or (
                status == "lower" and currentKey != currentKey.lower()
            ):
                status = "mixed"
                return
            else:
                return

        process_keys(idx + 1)

    process_keys(0)

    return status == "upper" or status == "lower"