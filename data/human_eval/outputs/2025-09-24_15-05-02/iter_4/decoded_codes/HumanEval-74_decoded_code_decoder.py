def total_match(lst1, lst2):
    total_length1 = 0
    for string in lst1:
        total_length1 += len(string)

    total_length2 = 0
    for string in lst2:
        total_length2 += len(string)

    if total_length1 <= total_length2:
        return lst1
    else:
        return lst2