def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1
    ans = -1
    for index in range(1, len(frq)):
        if frq[index] >= index:
            ans = index
    return ans