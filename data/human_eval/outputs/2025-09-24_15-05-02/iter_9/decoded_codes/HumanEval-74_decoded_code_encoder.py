def total_match(lst1, lst2):
    total_length_lst1 = 0
    for string in lst1:
        total_length_lst1 += len(string)
    total_length_lst2 = 0
    for string in lst2:
        total_length_lst2 += len(string)
    if total_length_lst1 <= total_length_lst2:
        return lst1
    else:
        return lst2