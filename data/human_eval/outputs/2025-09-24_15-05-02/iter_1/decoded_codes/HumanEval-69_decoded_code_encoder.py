def find_ans(lst):
    freq = [0] * (max(lst) + 1)
    for x in lst:
        freq[x] += 1
    ans = -1
    for i in range(1, len(freq)):
        if freq[i] >= i:
            ans = i
    return ans