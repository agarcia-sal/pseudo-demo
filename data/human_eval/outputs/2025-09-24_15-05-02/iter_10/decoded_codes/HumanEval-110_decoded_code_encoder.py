def exchange(lst1, lst2):
    odd = 0
    even = 0
    for number in lst1:
        if number % 2 == 1:
            odd += 1
    for number in lst2:
        if number % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"