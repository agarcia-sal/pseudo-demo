def exchange(list1, list2):
    odd = 0
    even = 0
    for element in list1:
        if element % 2 == 1:
            odd += 1
    for element in list2:
        if element % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"