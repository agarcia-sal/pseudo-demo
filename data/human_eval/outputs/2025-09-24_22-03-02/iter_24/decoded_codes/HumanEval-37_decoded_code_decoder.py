def sort_even(l: list):
    evens = []
    odds = []
    i = 0
    while i < len(l):
        evens.append(l[i])
        i += 2
    j = 1
    while j < len(l):
        odds.append(l[j])
        j += 2
    evens.sort()
    ans = []
    k = 0
    while k < len(evens) and k < len(odds):
        ans.extend([evens[k], odds[k]])
        k += 1
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans