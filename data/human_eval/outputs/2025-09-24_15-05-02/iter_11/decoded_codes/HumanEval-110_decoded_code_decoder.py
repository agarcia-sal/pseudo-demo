def exchange(list1, list2):
    odd_count = 0
    even_count = 0

    for element in list1:
        if element % 2 == 1:
            odd_count += 1

    for element in list2:
        if element % 2 == 0:
            even_count += 1

    if even_count >= odd_count:
        return "YES"

    return "NO"