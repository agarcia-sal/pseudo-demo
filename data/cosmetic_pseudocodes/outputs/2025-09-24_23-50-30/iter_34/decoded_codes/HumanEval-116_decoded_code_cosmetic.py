from typing import List

def sort_array(list_of_numbers: List[int]) -> List[int]:
    interim_list = sorted(list_of_numbers)

    def count_ones(s: str) -> int:
        total = 0
        idx = 0
        while idx < len(s):
            if s[idx] == '1':
                total += 1
            idx += 1
        return total

    def key_func(num: int) -> int:
        bin_rep = bin(num)[2:]
        return count_ones(bin_rep)

    sorted_final = sorted(interim_list, key=key_func)
    return sorted_final