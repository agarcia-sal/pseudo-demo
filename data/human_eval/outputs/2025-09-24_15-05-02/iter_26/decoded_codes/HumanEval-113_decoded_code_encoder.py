from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result: List[str] = []
    for string in list_of_strings:
        count_odd: int = sum(1 for ch in string if ch.isdigit() and int(ch) % 2 == 1)
        result.append(
            f"the number of odd elements {count_odd}n the str{count_odd}ng {count_odd} of the {count_odd}nput."
        )
    return result