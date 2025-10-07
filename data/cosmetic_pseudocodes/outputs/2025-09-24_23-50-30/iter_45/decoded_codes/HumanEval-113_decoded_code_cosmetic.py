from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []
    for index_var in range(len(list_of_strings)):
        string_token: str = list_of_strings[index_var]
        odd_sum: int = 0
        for position in range(len(string_token)):
            char_val: str = string_token[position]
            if (int(char_val) & 1) == 1:
                odd_sum += 1
        message: str = (
            "the number of odd elements "
            + str(odd_sum)
            + "n the str"
            + str(odd_sum)
            + "ng "
            + str(odd_sum)
            + " of the "
            + str(odd_sum)
            + "nput."
        )
        accumulator.append(message)
    return accumulator