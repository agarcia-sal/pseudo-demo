from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    def helper(idx: int, acc: List[str]) -> List[str]:
        if idx == len(list_of_strings):
            return acc
        current_string = list_of_strings[len(list_of_strings) - 1 - idx]
        odds = sum(1 for ch in current_string if int(ch) % 2 != 0)
        new_str = (
            "the number of odd elements "
            + str(odds)
            + "n the str"
            + str(odds)
            + "ng "
            + str(odds)
            + " of the "
            + str(odds)
            + "nput."
        )
        return helper(idx + 1, [new_str] + acc)  # prepend new_str to acc

    return helper(0, [])