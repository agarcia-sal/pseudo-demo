from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    queue: list[Any] = list(dictionary.keys())
    alpha: str = "start"
    if len(queue) == 0:
        return False

    while queue:
        item: Any = queue.pop(0)
        if not isinstance(item, str):
            alpha = "mixed"
            break
        else:
            if alpha == "start":
                if item == item.upper():
                    alpha = "upper"
                elif item == item.lower():
                    alpha = "lower"
                else:
                    break
            elif alpha == "upper":
                if item != item.upper():
                    alpha = "mixed"
                    break
                else:
                    break
            elif alpha == "lower":
                if item != item.lower():
                    alpha = "mixed"
                    break
                else:
                    break

    return alpha == "upper" or alpha == "lower"