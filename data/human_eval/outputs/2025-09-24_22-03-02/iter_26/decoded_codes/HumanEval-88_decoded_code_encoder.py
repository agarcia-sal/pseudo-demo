def sort_array(array):
    if len(array) == 0:
        return [[]]
    sum_value = array[0] + array[len(array)-1]
    is_even = sum_value % 2 == 0
    result_list = []
    for index in range(len(array)):
        result_list.append(array[index])
    if is_even:
        sort_list_descending(result_list)
    else:
        sort_list_ascending(result_list)
    return result_list

def sort_list_ascending(list_to_sort):
    for i in range(len(list_to_sort)-1):
        for j in range(len(list_to_sort)-1 - i):
            if list_to_sort[j] > list_to_sort[j+1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j+1]
                list_to_sort[j+1] = temp

def sort_list_descending(list_to_sort):
    for i in range(len(list_to_sort)-1):
        for j in range(len(list_to_sort)-1 - i):
            if list_to_sort[j] < list_to_sort[j+1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j+1]
                list_to_sort[j+1] = temp