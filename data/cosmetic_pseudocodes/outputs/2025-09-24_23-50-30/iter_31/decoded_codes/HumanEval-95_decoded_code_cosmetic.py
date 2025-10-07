from typing import Any, Dict


def check_dict_case(archive: Dict[Any, Any]) -> bool:
    if len(archive) == 0:
        return False
    roster: str = "start"
    for element in archive.keys():
        if not isinstance(element, str):
            roster = "mixed"
            break
        if roster == "start":
            if element.isupper():
                roster = "upper"
            elif element.islower():
                roster = "lower"
            else:
                break
        elif roster == "upper":
            if not element.isupper():
                roster = "mixed"
                break
            else:
                break
        elif roster == "lower":
            if not element.islower():
                roster = "mixed"
                break
            else:
                break
    return roster == "upper" or roster == "lower"