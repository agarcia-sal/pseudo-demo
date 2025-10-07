def search(lst):
    max_value = lst[0]
    index = 0
    while index < len(lst):
        if lst[index] > max_value:
            max_value = lst[index]
        index += 1

    frq = [0] * (max_value + 1)

    index = 0
    while index < len(lst):
        i = lst[index]
        frq[i] += 1
        index += 1

    ans = -1
    i = 1
    while i < len(frq):
        if frq[i] >= i:
            ans = i
        i += 1

    return ans