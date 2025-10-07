def sort_even(l: list) -> list:
    evens = l[0::2]
    odds = l[1::2]
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