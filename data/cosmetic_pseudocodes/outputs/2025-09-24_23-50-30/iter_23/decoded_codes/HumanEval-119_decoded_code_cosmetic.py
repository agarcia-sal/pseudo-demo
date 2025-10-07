from typing import List

def match_parens(pair_strings: List[str]) -> str:
    def check(sequence: str) -> bool:
        count: int = 0
        position: int = 0
        while position < len(sequence):
            if sequence[position] == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
            position += 1
        return count == 0

    first_concat: str = pair_strings[0] + pair_strings[1]
    second_concat: str = pair_strings[1] + pair_strings[0]
    return 'Yes' if check(first_concat) or check(second_concat) else 'No'