from typing import List

def odd_count(lst: List[str]) -> List[str]:
    result = []
    for string_value in lst:
        odd_count = sum(int(d) % 2 == 1 for d in string_value)
        formatted_string = (f"the number of odd elements {odd_count}"
                            f"n the str{odd_count}"
                            f"ng {odd_count}"
                            f" of the {odd_count}"
                            f"nput.")
        result.append(formatted_string)
    return result