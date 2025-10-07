from typing import List


def parse_nested_parens(str_input: str) -> List[int]:
    def parse_paren_group(sub_str: str) -> int:
        def loop(index: int, curr: int, maxd: int) -> int:
            if index == len(sub_str):
                return maxd
            if sub_str[index] == '(':
                curr += 1
                maxd = max(curr, maxd)
            else:
                curr -= 1
            return loop(index + 1, curr, maxd)
        return loop(0, 0, 0)

    tokens = [x for x in str_input.split(" ") if x != ""]
    return [parse_paren_group(t) for t in tokens]