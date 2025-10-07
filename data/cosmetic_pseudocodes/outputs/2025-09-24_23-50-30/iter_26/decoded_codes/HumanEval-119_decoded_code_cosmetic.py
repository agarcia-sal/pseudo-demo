from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(sequence: str) -> bool:
        def helper(index: int, accumulator: int) -> bool:
            if index == len(sequence):
                return accumulator == 0
            ch = sequence[index]
            new_acc = accumulator + 1 if ch == '(' else accumulator - 1
            if new_acc < 0:
                return False
            return helper(index + 1, new_acc)
        return helper(0, 0)

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return "Yes"
    if check(second_concat):
        return "Yes"
    return "No"