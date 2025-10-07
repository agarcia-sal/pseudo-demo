from typing import Dict, Tuple


def even_odd_palindrome(n_param: int) -> Tuple[int, int]:
    def is_palindrome(test_val: int) -> bool:
        str_val = str(test_val)
        rev_str_val = "".join(str_val[idx] for idx in range(len(str_val) - 1, -1, -1))
        return str_val == rev_str_val

    accumulator: Dict[str, int] = {"even_count": 0, "odd_count": 0}

    def process_next(curr: int, limit: int, acc: Dict[str, int]) -> Dict[str, int]:
        if curr > limit:
            return acc
        remainder = curr % 2
        palindrome_check = is_palindrome(curr)
        if palindrome_check:
            if remainder == 0:
                acc["even_count"] += 1
            else:
                acc["odd_count"] += 1
        return process_next(curr + 1, limit, acc)

    final_counts = process_next(1, n_param, accumulator)
    return final_counts["even_count"], final_counts["odd_count"]