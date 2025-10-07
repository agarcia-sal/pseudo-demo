def sort_even(l: list):
    evens = l[0::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for i in range(len(odds)):
        e = evens[i]
        o = odds[i]
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[len(evens) - 1])
    return ans