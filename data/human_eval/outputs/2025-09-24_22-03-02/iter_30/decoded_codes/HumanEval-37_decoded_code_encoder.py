def sort_even(l: list) -> list:
    evens = []
    odds = []
    index = 0
    while index < len(l):
        if index % 2 == 0:
            evens.append(l[index])
        index += 1
    index = 1
    while index < len(l):
        odds.append(l[index])
        index += 2
    evens.sort()
    ans = []
    index = 0
    limit = min(len(evens), len(odds))
    while index < limit:
        ans.append(evens[index])
        ans.append(odds[index])
        index += 1
    if len(evens) > len(odds):
        ans.append(evens[len(evens) - 1])
    return ans