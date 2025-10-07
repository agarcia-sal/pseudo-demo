def sort_even(lst):
    # Extract elements at even indices
    evens = lst[0::2]
    # Extract elements at odd indices
    odds = lst[1::2]

    # Sort the evens in ascending order
    evens.sort()

    ans = []
    # Iterate over pairs of evens and odds
    for e, o in zip(evens, odds):
        ans.append(e)
        ans.append(o)

    # If there are more evens than odds, append the last even
    if len(evens) > len(odds):
        ans.append(evens[-1])

    return ans