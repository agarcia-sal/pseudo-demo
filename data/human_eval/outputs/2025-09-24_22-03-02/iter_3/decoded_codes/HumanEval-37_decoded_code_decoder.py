def sort_even(l):
    evens = sorted(l[::2])
    odds = l[1::2]
    ans = [x for pair in zip(evens, odds) for x in pair]
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans