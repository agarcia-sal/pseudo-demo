def search(lst) -> int:
    frq = []
    max_value = 0
    for index in range(len(lst)):
        element = lst[index]
        if element > max_value:
            max_value = element
    for index in range(max_value + 1):
        frq.append(0)
    for index in range(len(lst)):
        element = lst[index]
        frq[element] += 1
    ans = -1
    for i in range(1, len(frq)):
        frq_i = frq[i]
        if frq_i >= i:
            ans = i
    return ans