def sort_even(l):
    evens = sorted(l[::2])
    odds = l[1::2]
    ans = []
    for e, o in zip(evens, odds):
        ans.append(e)
        ans.append(o)
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans