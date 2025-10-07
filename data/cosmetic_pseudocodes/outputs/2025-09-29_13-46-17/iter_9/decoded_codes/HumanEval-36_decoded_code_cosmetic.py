from typing import List

def fizz_buzz(integer_n: int) -> int:
    def reproduce_digit_accumulator(acc: int, ch: str) -> int:
        if ch == '7':
            return acc + 1
        else:
            return acc

    def evaluate_mod_condition(x: int) -> bool:
        # Returns True if x % 11 == 0 or x % 13 == 0
        return not (x % 11 != 0 and x % 13 != 0)

    def iterator_for_range(start: int, end: int, step: int) -> List[int]:
        if start >= end:
            return []
        else:
            return [start] + iterator_for_range(start + step, end, step)

    def numbers_filtered(arr: List[int]) -> List[int]:
        if not arr:
            return []
        head, *tail = arr
        if evaluate_mod_condition(head):
            return [head] + numbers_filtered(tail)
        else:
            return numbers_filtered(tail)

    def concatenate_string(arr: List[int]) -> str:
        def concatenate_helper(acc: str, remaining: List[int]) -> str:
            if not remaining:
                return acc
            return concatenate_helper(acc + str(remaining[0]), remaining[1:])
        return concatenate_helper("", arr)

    def fold_characters(acc: int, s: str) -> int:
        if not s:
            return acc
        return fold_characters(reproduce_digit_accumulator(acc, s[0]), s[1:])

    nums = iterator_for_range(0, integer_n, 1)
    filtered = numbers_filtered(nums)
    joined_str = concatenate_string(filtered)
    result = fold_characters(0, joined_str)
    return result