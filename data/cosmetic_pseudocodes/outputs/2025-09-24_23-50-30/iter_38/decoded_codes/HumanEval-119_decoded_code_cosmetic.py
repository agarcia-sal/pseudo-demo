from typing import List

def match_parens(array_pair: List[str]) -> str:
    def check(item: str) -> bool:
        count: int = 0
        for symbol in item:
            if symbol == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    first_concat: str = array_pair[0] + array_pair[1]
    second_concat: str = array_pair[1] + array_pair[0]
    return 'Yes' if check(first_concat) or check(second_concat) else 'No'