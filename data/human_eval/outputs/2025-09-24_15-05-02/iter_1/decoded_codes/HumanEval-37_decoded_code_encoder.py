def sort_even(l):
    evens = sorted(l[::2])
    odds = l[1::2]
    ans = []
    for e, o in zip(evens, odds):
        ans += [e, o]
    if len(evens) > len(odds):
        ans += [evens[-1]]
    return ans