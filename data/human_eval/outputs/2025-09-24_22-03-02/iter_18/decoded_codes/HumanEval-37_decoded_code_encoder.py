def sort_even(l: list):
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
    while i < min(len(evens), len(odds)):
        ans.append(evens[i])
        ans.append(odds[i])
        i += 1
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans