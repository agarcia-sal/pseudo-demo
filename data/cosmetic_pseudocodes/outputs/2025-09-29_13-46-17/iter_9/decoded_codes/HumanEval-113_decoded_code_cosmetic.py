from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    def is_odd(n: int) -> int:
        return 1 if n % 2 != 0 else 0

    def sum_odds(acc: int, chars: List[str]) -> int:
        if not chars:
            return acc
        return sum_odds(acc + is_odd(int(chars[0])), chars[1:])

    def process_strings(strings: List[str]) -> List[str]:
        if not strings:
            return []
        count_odd = sum_odds(0, list(strings[0]))
        result_str = (
            "the number of odd elements "
            + str(count_odd)
            + "n the str"
            + str(count_odd)
            + "ng "
            + str(count_odd)
            + " of the "
            + str(count_odd)
            + "nput."
        )
        return [result_str] + process_strings(strings[1:])

    return process_strings(list_of_strings)