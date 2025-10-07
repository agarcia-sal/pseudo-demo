from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens: List[int] = []
    odds: List[int] = []
    ans: List[int] = []
    index = 0
    while index < len(l):
        evens.append(l[index])
        index += 2
    index = 1
    while index < len(l):
        odds.append(l[index])
        index += 2
    evens.sort()
    index = 0
    while index < len(odds):
        ans.extend([evens[index], odds[index]])
        index += 1
    if len(evens) > len(odds):
        ans.append(evens[len(evens) - 1])
    return ans