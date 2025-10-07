from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        odd_count: int = sum(1 for ch in string_element if ch.isdigit() and int(ch) % 2 == 1)
        sentence = (
            "the number of odd elements "
            + str(odd_count)
            + "n the str"
            + str(odd_count)
            + "ng "
            + str(odd_count)
            + " of the "
            + str(odd_count)
            + "nput."
        )
        result_list.append(sentence)
    return result_list