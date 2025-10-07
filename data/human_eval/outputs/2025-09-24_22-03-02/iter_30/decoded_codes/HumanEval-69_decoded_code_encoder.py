def search(lst):
    max_value = lst[0]
    for index in range(1, len(lst)):
        if lst[index] > max_value:
            max_value = lst[index]

    frq = [0] * (max_value + 1)
    for i in lst:
        frq[i] += 1

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i

    return ans