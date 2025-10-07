def total_match(list1, list2):
    length1 = sum(len(string) for string in list1)
    length2 = sum(len(string) for string in list2)
    if length1 <= length2:
        return list1
    else:
        return list2