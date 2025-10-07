from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens = []
    odds = []
    index = 0
    while index < len(l):
        evens.append(l[index])
        index += 2
    index = 1
    while index < len(l):
        odds.append(l[index])
        index += 2
    evens.sort()
    ans = []
    i = 0
    while i < len(odds):
        ans.append(evens[i])
        ans.append(odds[i])
        i += 1
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans