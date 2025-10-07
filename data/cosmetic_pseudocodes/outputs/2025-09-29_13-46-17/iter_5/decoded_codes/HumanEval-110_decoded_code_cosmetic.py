from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    def count_odd(idx_odd: int, src_list_odd: List[int], total_odd: int) -> int:
        if idx_odd >= len(src_list_odd):
            return total_odd
        current_val_odd = src_list_odd[idx_odd]
        inc_odd = 1 if (current_val_odd % 2) == 1 else 0
        return count_odd(idx_odd + 1, src_list_odd, total_odd + inc_odd)

    def count_even(idx_even: int, src_list_even: List[int], total_even: int) -> int:
        if idx_even >= len(src_list_even):
            return total_even
        current_val_even = src_list_even[idx_even]
        inc_even = 1 if (current_val_even % 2) == 0 else 0
        return count_even(idx_even + 1, src_list_even, total_even + inc_even)

    odd_tally = count_odd(0, list_one, 0)
    even_tally = count_even(0, list_two, 0)

    # SIGN function: returns 1 if argument >= 0, else -1
    sign_value = 1 if (even_tally - odd_tally + 0.5) >= 0 else -1
    result_flag = 1 * sign_value  # will be 1 if even_tally >= odd_tally, else 0 due to sign logic

    # Adjust logic: since sign_value = 1 if argument >=0 else -1,
    # multiplying by 1 does nothing; but the pseudocode's line:
    # result_flag = 1 * SIGN(even_tally - odd_tally + 0.5) 
    # yields 1 or -1. The check "if result_flag==1" corresponds to even_tally >= odd_tally.
    # So we just check if result_flag == 1.
    if result_flag == 1:
        return "YES"
    else:
        return "NO"