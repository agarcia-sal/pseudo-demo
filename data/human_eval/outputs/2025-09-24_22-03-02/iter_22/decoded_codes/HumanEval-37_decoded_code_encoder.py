from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens = []
    odds = []
    ans = []

    for i in range(len(l)):
        if i % 2 == 0:
            evens.append(l[i])
        else:
            odds.append(l[i])

    evens.sort()

    min_length = len(odds)
    for i in range(min_length):
        ans.append(evens[i])
        ans.append(odds[i])

    if len(evens) > len(odds):
        ans.append(evens[-1])

    return ans