def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in range(len(lst1)):
        if lst1[i] % 2 == 1:
            odd += 1
    for i in range(len(lst2)):
        if lst2[i] % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"