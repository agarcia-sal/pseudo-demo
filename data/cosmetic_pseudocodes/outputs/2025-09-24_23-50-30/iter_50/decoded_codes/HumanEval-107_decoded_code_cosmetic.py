from typing import Dict, Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        str_repr = str(number)
        rev_str = ''.join(str_repr[idx] for idx in range(len(str_repr) - 1, -1, -1))
        return rev_str == str_repr

    def count_palindromes(current: int, limit: int, counts: Dict[str, int]) -> Dict[str, int]:
        if current > limit:
            return counts
        if is_palindrome(current):
            if current % 2 == 0:
                counts["even"] += 1
            else:
                counts["odd"] += 1
        return count_palindromes(current + 1, limit, counts)

    count_storage: Dict[str, int] = {"even": 0, "odd": 0}
    final_counts = count_palindromes(1, n, count_storage)
    return final_counts["even"], final_counts["odd"]