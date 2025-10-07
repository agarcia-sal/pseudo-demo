def add(lst):
    sum_result = 0
    length_lst = len(lst)
    index = 1
    while index < length_lst:
        element = lst[index]
        if element % 2 == 0:
            sum_result += element
        index += 2
    return sum_result