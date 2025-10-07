from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    dict1: Dict[str, int] = {}
    list1 = test_string.split(' ')
    maximum_count = 0

    for element in list1:
        if element and list1.count(element) > maximum_count:
            maximum_count = list1.count(element)

    if maximum_count > 0:
        for element in list1:
            if list1.count(element) == maximum_count:
                dict1[element] = maximum_count
    return dict1