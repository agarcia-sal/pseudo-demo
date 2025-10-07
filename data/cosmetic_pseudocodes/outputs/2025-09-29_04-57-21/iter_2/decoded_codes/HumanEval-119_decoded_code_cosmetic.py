from typing import List

def match_parens(paired_strings: List[str]) -> str:
    def verify(expr: str) -> bool:
        net_count: int = 0
        for symbol in expr:
            if symbol == '(':
                net_count += 1
            else:
                net_count -= 1
            if net_count < 0:
                return False
        return net_count == 0

    comboA = paired_strings[0] + paired_strings[1]
    comboB = paired_strings[1] + paired_strings[0]
    if verify(comboA) or verify(comboB):
        return 'Yes'
    return 'No'