from typing import List


def string_sequence(integer_n: int) -> str:
    def _gen_interval(curr_val: int, limit: int, acc: List[str]) -> List[str]:
        if curr_val > limit:
            return acc
        return _gen_interval(curr_val + 1, limit, acc + [str(curr_val)])

    generated_list: List[str] = _gen_interval(0, integer_n, [])
    separator: str = " "
    result_acc: str = ""

    def _join_with_space(items: List[str], idx: int) -> str:
        nonlocal result_acc
        if idx >= len(items):
            return result_acc
        delimiter: str = "" if idx == 0 else separator
        result_acc = result_acc + delimiter + items[idx]
        return _join_with_space(items, idx + 1)

    return _join_with_space(generated_list, 0)