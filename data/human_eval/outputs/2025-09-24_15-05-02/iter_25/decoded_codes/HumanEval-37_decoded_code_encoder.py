from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    evens: List[int] = sorted(list_l[0::2])
    odds: List[int] = list_l[1::2]
    ans: List[int] = []

    for even_val, odd_val in zip(evens, odds):
        ans.extend([even_val, odd_val])

    if len(evens) > len(odds):
        ans.append(evens[-1])

    return ans