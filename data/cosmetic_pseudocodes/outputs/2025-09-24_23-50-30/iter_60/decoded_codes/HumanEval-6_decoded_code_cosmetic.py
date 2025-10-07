from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def depth_tail_recursion(idx: int, cur_d: int, max_d: int) -> int:
            if idx >= len(group_string):
                return max_d
            if group_string[idx] == '(':
                new_cur = cur_d + 1
                new_max = new_cur if new_cur > max_d else max_d
                return depth_tail_recursion(idx + 1, new_cur, new_max)
            else:
                return depth_tail_recursion(idx + 1, cur_d - 1, max_d)

        return depth_tail_recursion(0, 0, 0)

    def filter_and_map(arr: List[str], fn) -> List[int]:
        def inner_fm(i: int, acc: List[int]) -> List[int]:
            if i >= len(arr):
                return acc
            elt = arr[i]
            if elt != "":
                return inner_fm(i + 1, acc + [fn(elt)])
            else:
                return inner_fm(i + 1, acc)
        return inner_fm(0, [])

    split_groups = parentheses_string.split(' ')
    return filter_and_map(split_groups, parse_paren_group)