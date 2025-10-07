from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens = l[0::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for even_element, odd_element in zip(evens, odds):
        ans.append(even_element)
        ans.append(odd_element)
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans