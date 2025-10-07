from typing import List, Callable


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def aux_layer(acc_depth: int, acc_max: int, chars_list: List[str]) -> int:
            if not chars_list:
                return acc_max
            front_char, rest_chars = chars_list[0], chars_list[1:]
            if front_char == '(':
                new_depth = acc_depth + 1
                new_max = new_depth if new_depth > acc_max else acc_max
                return aux_layer(new_depth, new_max, rest_chars)
            else:
                new_depth = acc_depth - 1
                return aux_layer(new_depth, acc_max, rest_chars)

        return aux_layer(0, 0, list(group_string))

    def split_chars(s: str) -> List[str]:
        acc: List[str] = []
        temp: str = ""
        idx: int = 0

        def split_helper() -> List[str]:
            nonlocal acc, temp, idx
            if idx >= len(s):
                if temp != "":
                    acc.append(temp)
                return acc
            elif s[idx] == ' ':
                if temp != "":
                    acc.append(temp)
                temp_clear = ""
                idx_inc = idx + 1
                temp, idx = temp_clear, idx_inc
                return split_helper()
            else:
                temp += s[idx]
                idx += 1
                return split_helper()

        return split_helper()

    def filter_nonempty(lst: List[str]) -> List[str]:
        if not lst:
            return []
        if lst[0] != "":
            return [lst[0]] + filter_nonempty(lst[1:])
        else:
            return filter_nonempty(lst[1:])

    def apply_map(func: Callable[[str], int], lst: List[str]) -> List[int]:
        if not lst:
            return []
        return [func(lst[0])] + apply_map(func, lst[1:])

    chunks = filter_nonempty(split_chars(parentheses_string))
    return apply_map(parse_paren_group, chunks)