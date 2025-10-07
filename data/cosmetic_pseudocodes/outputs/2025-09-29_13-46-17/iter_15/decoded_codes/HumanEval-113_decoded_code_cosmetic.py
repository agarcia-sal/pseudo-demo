from typing import List, Callable

def odd_count(list_of_strings: List[str]) -> List[str]:
    def combine(a: List[str], b: str) -> List[str]:
        return a + [b]

    def count_odd_digits(s: str, i: int, acc: int) -> int:
        if i < 0:
            return acc
        digit_val = int(s[i])
        is_odd = (digit_val % 2) != 0
        new_acc = acc + 1 if is_odd else acc
        return count_odd_digits(s, i - 1, new_acc)

    def build_string(x: int) -> str:
        # Constructs the string as detailed in the pseudocode concatenations
        return (
            "the number of odd elements "
            + str(x)
            + "n the str"
            + str(x)
            + "ng "
            + str(x)
            + " of the "
            + "nput."
        )

    def acc_result(lst: List[str], idx: int, acc: List[str]) -> List[str]:
        if idx == len(lst):
            return acc
        current_str = lst[idx]
        odds_count = count_odd_digits(current_str, len(current_str) - 1, 0)
        created_str = build_string(odds_count)
        return acc_result(lst, idx + 1, combine(acc, created_str))

    return acc_result(list_of_strings, 0, [])