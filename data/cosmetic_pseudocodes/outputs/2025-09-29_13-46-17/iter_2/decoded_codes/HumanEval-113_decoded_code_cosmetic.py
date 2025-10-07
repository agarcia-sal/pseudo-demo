from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    res: List[str] = []

    def process_index(i: int) -> None:
        if i >= len(list_of_strings):
            return
        current_string: str = list_of_strings[i]

        def count_odds(pos: int, acc: int) -> int:
            if pos >= len(current_string):
                return acc
            ch: str = current_string[pos]
            val: int = int(ch)
            return count_odds(pos + 1, acc + (1 if val % 2 != 0 else 0))

        odd_num: int = count_odds(0, 0)
        res.append(
            f"the number of odd elements {odd_num}n the str{odd_num}ng {odd_num} of the {odd_num}nput."
        )
        process_index(i + 1)

    process_index(0)
    return res