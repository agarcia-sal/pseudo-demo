from typing import List

def match_parens(array_pair: List[str]) -> str:
    def check(str_val: str) -> bool:
        def validate(index: int, count: int) -> bool:
            if index >= len(str_val):
                return count == 0
            if count < 0:
                return False
            delta = 1 if str_val[index] == '(' else -1
            return validate(index + 1, count + delta)
        return validate(0, 0)

    combined_a = array_pair[0] + array_pair[1]
    combined_b = array_pair[1] + array_pair[0]
    if check(combined_a) or check(combined_b):
        return 'Yes'
    return 'No'