from typing import NamedTuple, Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    class PalindromeCounts(NamedTuple):
        even_count: int
        odd_count: int

    def is_palindrome(number: int) -> bool:
        s = str(number)

        def recursive_compare(start_index: int, end_index: int) -> bool:
            if start_index >= end_index:
                return True
            return (s[start_index] == s[end_index]) and recursive_compare(start_index + 1, end_index - 1)

        return recursive_compare(0, len(s) - 1)

    def fold_over_range(current: int, limit: int, acc: PalindromeCounts) -> PalindromeCounts:
        if current > limit:
            return acc
        mod_value = current % 2
        if is_palindrome(current):
            if mod_value == 1:
                acc1 = PalindromeCounts(even_count=acc.even_count, odd_count=acc.odd_count + 1)
            elif mod_value == 0:
                acc1 = PalindromeCounts(even_count=acc.even_count + 1, odd_count=acc.odd_count)
            else:
                acc1 = acc  # Defensive, though mod_value always 0 or 1
        else:
            acc1 = acc
        return fold_over_range(current + 1, limit, acc1)

    initial_accumulator = PalindromeCounts(even_count=0, odd_count=0)
    final_result = fold_over_range(1, n, initial_accumulator)
    return final_result.even_count, final_result.odd_count