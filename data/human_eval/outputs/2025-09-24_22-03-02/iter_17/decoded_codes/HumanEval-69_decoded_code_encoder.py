def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1
    ans = -1
    index = 1
    while index < len(frq):
        if frq[index] >= index:
            ans = index
        index += 1
    return ans