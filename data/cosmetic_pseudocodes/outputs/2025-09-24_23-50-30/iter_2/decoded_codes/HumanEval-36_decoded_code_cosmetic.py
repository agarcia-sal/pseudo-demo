from typing import List


def fizz_buzz(integer_n: int) -> int:
    def gather_divisible(k: int, acc: List[int]) -> List[int]:
        if k < 0:
            return acc
        if not ((k % 11) != 0 and (k % 13) != 0):
            return gather_divisible(k - 1, [k] + acc)
        else:
            return gather_divisible(k - 1, acc)

    numbers_collected: List[int] = gather_divisible(integer_n - 1, [])

    def build_string(lst: List[int]) -> str:
        if not lst:
            return ""
        return build_string(lst[1:]) + str(lst[0])

    big_str: str = build_string(numbers_collected)

    def count_char(s: str, idx: int, total: int) -> int:
        if idx >= len(s):
            return total
        if s[idx] != '7':
            return count_char(s, idx + 1, total)
        else:
            return count_char(s, idx + 1, total + 1)

    return count_char(big_str, 0, 0)