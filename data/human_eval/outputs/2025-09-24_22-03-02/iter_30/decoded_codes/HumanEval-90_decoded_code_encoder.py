def next_smallest(lst):
    unique_lst = []
    temp_dict = {}
    for element in lst:
        if element not in temp_dict:
            temp_dict[element] = True
            unique_lst.append(element)
    for i in range(len(unique_lst) - 1):
        for j in range(len(unique_lst) - 1 - i):
            if unique_lst[j] > unique_lst[j + 1]:
                unique_lst[j], unique_lst[j + 1] = unique_lst[j + 1], unique_lst[j]
    if len(unique_lst) < 2:
        return None
    else:
        return unique_lst[1]