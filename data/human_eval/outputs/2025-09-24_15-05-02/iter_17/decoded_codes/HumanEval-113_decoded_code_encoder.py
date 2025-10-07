from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result: List[str] = []
    for string_element in list_of_strings:
        n: int = sum(1 for d in string_element if d.isdigit() and int(d) % 2 == 1)
        result.append(f"the number of odd elements {n}n the str{n}ng {n} of the {n}nput.")
    return result