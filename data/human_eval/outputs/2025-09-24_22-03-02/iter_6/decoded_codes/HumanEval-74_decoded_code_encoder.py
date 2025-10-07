def total_match(lst1, lst2):
    length1 = sum(len(string) for string in lst1)
    length2 = sum(len(string) for string in lst2)
    if length1 <= length2:
        return lst1
    else:
        return lst2