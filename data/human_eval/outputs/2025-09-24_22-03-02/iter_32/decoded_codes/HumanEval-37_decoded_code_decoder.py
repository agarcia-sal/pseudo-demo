from typing import List

def sort_even(l: List) -> List:
    evens = []
    odds = []
    index = 0
    while index < len(l):
        if index % 2 == 0:
            evens.append(l[index])
        else:
            odds.append(l[index])
        index += 1
    evens.sort()
    ans = []
    i = 0
    evens_length = len(evens)
    odds_length = len(odds)
    while i < odds_length:
        ans.append(evens[i])
        ans.append(odds[i])
        i += 1
    if evens_length > odds_length:
        ans.append(evens[evens_length - 1])
    return ans