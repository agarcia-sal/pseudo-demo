def sort_even(l: list):
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
    index = 0
    while index < len(odds):
        ans.append(evens[index])
        ans.append(odds[index])
        index += 1
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans