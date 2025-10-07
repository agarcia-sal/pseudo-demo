from typing import List, Optional, Tuple


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def recurse_chars(chars: str, index: int) -> Tuple[int, int]:
            if not (index < len(chars)):
                return 0, 0
            else:
                open_count, max_depth = recurse_chars(chars, index + 1)
                c = chars[index]
                # If c == '(', increment open_count and update max_depth; else (must be ')') decrement open_count
                if (c == '('):
                    open_count += 1
                    max_depth = max(open_count, max_depth)
                else:
                    open_count -= 1
                return open_count, max_depth

        _, max_depth = recurse_chars(group_string, 0)
        return max_depth

    def map_filter_lambda(func, arr: List[str]) -> List[int]:
        def helper(i: int) -> List[int]:
            if i < len(arr):
                res = func(arr[i])
                if res is not None:
                    return [res] + helper(i + 1)
                else:
                    return helper(i + 1)
            else:
                return []
        return helper(0)

    groups = parentheses_string.split(' ')
    return map_filter_lambda(lambda g: parse_paren_group(g) if g != '' else None, groups)