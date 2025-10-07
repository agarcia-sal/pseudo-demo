from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    dict1: Dict[str, int] = {}
    list1: list[str] = test.split(" ")
    t: int = 0

    for i in list1:
        if i and list1.count(i) > t:
            t = list1.count(i)

    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t

    return dict1