def sort_even(l: list) -> list:
    evens = []
    odds = []
    length_l = len(l)
    index = 0
    while index < length_l:
        if index % 2 == 0:
            evens.append(l[index])
        index += 1
    index = 1
    while index < length_l:
        odds.append(l[index])
        index += 2
    evens.sort()
    ans = []
    length_odds = len(odds)
    index = 0
    while index < length_odds:
        ans.extend([evens[index], odds[index]])
        index += 1
    if len(evens) > len(odds):
        ans.append(evens[len(evens) - 1])
    return ans