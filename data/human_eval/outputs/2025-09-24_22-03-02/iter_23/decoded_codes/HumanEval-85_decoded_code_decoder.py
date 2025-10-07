def add(lst):
    total = 0
    length_of_lst = len(lst)
    index = 1
    while index < length_of_lst:
        element = lst[index]
        if element % 2 == 0:
            total += element
        index += 2
    return total