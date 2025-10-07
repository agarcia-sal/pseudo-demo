def sort_even(l: list) -> list:
    evens = []
    odds = []
    i = 0
    while i < len(l):
        if i % 2 == 0:
            evens.append(l[i])
        else:
            odds.append(l[i])
        i += 1
    evens.sort()
    ans = []
    j = 0
    while j < len(odds) and j < len(evens):
        ans.append(evens[j])
        ans.append(odds[j])
        j += 1
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans