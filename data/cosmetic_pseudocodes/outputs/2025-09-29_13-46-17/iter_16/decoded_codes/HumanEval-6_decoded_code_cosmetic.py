from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        length: int = len(group_string)

        def recur(i: int, acc_depth: int, max_d: int) -> int:
            if not (i < length):
                return max_d
            chr_ = group_string[i]
            new_depth = acc_depth + 1 if chr_ == '(' else acc_depth - 1
            new_max = new_depth if new_depth > max_d else max_d
            return recur(i + 1, new_depth, new_max)

        return recur(0, 0, 0)

    def reduce_fold(Lzʘ: List[str]) -> List[int]:
        if not Lzʘ:
            return []
        head, *tail = Lzʘ
        if head == "":
            return reduce_fold(tail)
        return [parse_paren_group(head)] + reduce_fold(tail)

    Ώβ = parentheses_string.split(" ")
    return reduce_fold(Ώβ)