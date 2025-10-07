def sort_even(l: list):
    evens = l[0::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.append(e)
        ans.append(o)
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans