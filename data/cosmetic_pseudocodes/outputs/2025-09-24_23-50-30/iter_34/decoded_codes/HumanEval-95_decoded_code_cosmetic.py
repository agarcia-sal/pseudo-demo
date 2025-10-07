from typing import Any, Dict, Iterator

def check_dict_case(container: Dict[Any, Any]) -> bool:
    flag: str = "start"
    elements = set(container.keys())
    if len(elements) == 0:
        return False
    iterator: Iterator[Any] = iter(elements)
    while True:
        try:
            member = next(iterator)
        except StopIteration:
            break
        if not isinstance(member, str):
            flag = "mixed"
            break
        if flag == "start":
            if member.isupper():
                flag = "upper"
            elif member.islower():
                flag = "lower"
            else:
                break
        elif flag == "upper":
            if not member.isupper():
                flag = "mixed"
                break
        elif flag == "lower":
            if not member.islower():
                flag = "mixed"
                break
        else:
            break
    return flag == "upper" or flag == "lower"