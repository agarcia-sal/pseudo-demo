def next_smallest(lst):
    S = sorted(set(lst))
    return None if len(S) < 2 else S[1]