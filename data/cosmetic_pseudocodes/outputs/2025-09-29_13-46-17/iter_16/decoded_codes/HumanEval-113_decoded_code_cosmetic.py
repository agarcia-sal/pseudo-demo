from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    results: List[str] = []
    index: int = 0
    while index < len(list_of_strings):
        s: str = list_of_strings[index]

        def count_odds(count: int, pos: int) -> int:
            if pos >= len(s):
                return count
            digit = int(s[pos])
            is_odd = (digit % 2) == 1
            return count_odds(count + (1 if is_odd else 0), pos + 1)

        odd_num: int = count_odds(0, 0)
        message = "the number of odd elements " + str(odd_num) + "n the str" + str(odd_num) + "ng " + str(odd_num) + " of the " + str(odd_num) + "nput."
        results.append(message)
        index += 1
    return results