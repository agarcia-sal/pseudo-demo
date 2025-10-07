from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    evens = [list_l[i] for i in range(0, len(list_l), 2)]
    odds = [list_l[i] for i in range(1, len(list_l), 2)]
    evens.sort()
    ans = []
    for even_elem, odd_elem in zip(evens, odds):
        ans.extend([even_elem, odd_elem])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans