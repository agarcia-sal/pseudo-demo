def exchange(lst1, lst2):
    odd_count = 0
    even_count = 0
    for element in lst1:
        if element % 2 == 1:
            odd_count += 1
    for element in lst2:
        if element % 2 == 0:
            even_count += 1
    if even_count >= odd_count:
        return "YES"
    return "NO"