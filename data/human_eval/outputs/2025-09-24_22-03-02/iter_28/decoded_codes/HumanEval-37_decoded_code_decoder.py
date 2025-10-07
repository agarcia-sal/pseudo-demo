def sort_even(l: list) -> list:
    evens = []
    odds = []
    i = 0
    while i < len(l):
        evens.append(l[i])
        i += 2
    i = 1
    while i < len(l):
        odds.append(l[i])
        i += 2
    evens.sort()
    ans = []
    index = 0
    while index < len(odds):
        ans.append(evens[index])
        ans.append(odds[index])
        index += 1
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans