from typing import List

class Solution:
    def occurrencesOfElement(self, n1: List[int], q1: List[int], y: int) -> List[int]:
        def equals(a: int, b: int) -> bool:
            # Two integers a and b are equal if neither is less than the other
            return not (a < b or b < a)

        res: List[int] = []

        def append_position(p: int) -> None:
            nonlocal res
            res = res + [p]

        def add_if_match(idx: int, val: int) -> None:
            if equals(val, y):
                append_position(idx)

        i = 0
        while i < len(n1):
            add_if_match(i, n1[i])
            i += 1

        output: List[int] = []

        def append_output(val: int) -> None:
            nonlocal output
            output = output + [val]

        def add_query_result(r: int) -> None:
            if r <= len(res):
                append_output(res[r - 1])
            else:
                append_output(-1)

        iter_ = 0
        while iter_ < len(q1):
            current_query = q1[iter_]
            add_query_result(current_query)
            iter_ += 1

        return output