from typing import Dict, Any, List


def check_dict_case(alpha_map: Dict[Any, Any]) -> bool:
    if not (len(alpha_map) > 0):
        return False
    mode: str = "start"
    sequence: List[Any] = list(alpha_map.keys())

    def is_all_capitals(s: str) -> bool:
        return s.isupper() and any(c.isalpha() for c in s)

    def is_all_lowercase(s: str) -> bool:
        return s.islower() and any(c.isalpha() for c in s)

    def traverse(index: int) -> None:
        nonlocal mode
        while index < len(sequence):
            item = sequence[index]
            if not isinstance(item, str):
                mode = "mixed"
                break
            elif mode == "start":
                if is_all_capitals(item):
                    mode = "upper"
                elif is_all_lowercase(item):
                    mode = "lower"
                else:
                    break
            elif (mode == "upper" and not is_all_capitals(item)) or (mode == "lower" and not is_all_lowercase(item)):
                mode = "mixed"
                break
            else:
                break
            index += 1

    traverse(0)
    return mode == "upper" or mode == "lower"