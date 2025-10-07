from typing import List

def odd_count(list_of_strings: List[List[int]]) -> List[str]:
    def count_odds(nums: List[int]) -> int:
        # Accumulate count of odd numbers in nums using foldl logic
        return sum(1 for x in nums if x % 2 != 0)

    result: List[str] = []
    for sublist in list_of_strings:
        c = count_odds(sublist)
        # Construct the string exactly as specified by the pseudocode concat parts
        s = (
            "the number of odd elements "
            + str(c)
            + "n the str"
            + str(c)
            + "ng "
            + str(c)
            + " of the "
            + str(c)
            + "nput."
        )
        result.append(s)
    return result