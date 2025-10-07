def sort_even(l: list) -> list:
    evens = []
    odds = []
    length_l = len(l)
    index = 0
    while index < length_l:
        evens.append(l[index])
        index += 2
    index = 1
    while index < length_l:
        odds.append(l[index])
        index += 2
    evens.sort()
    ans = []
    index = 0
    length_evens = len(evens)
    length_odds = len(odds)
    while index < length_odds:
        ans.append(evens[index])
        ans.append(odds[index])
        index += 1
    if length_evens > length_odds:
        ans.append(evens[length_evens - 1])
    return ans