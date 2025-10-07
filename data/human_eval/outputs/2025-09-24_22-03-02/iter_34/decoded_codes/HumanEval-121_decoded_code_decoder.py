def solution(lst):
    sum_result = 0
    index = 0
    while index < len(lst):
        element = lst[index]
        is_index_even = (index % 2) == 0
        is_element_odd = (element % 2) == 1
        if is_index_even and is_element_odd:
            sum_result += element
        index += 1
    return sum_result