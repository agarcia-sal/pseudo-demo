def solution(lst):
    total = 0
    length = len(lst)
    index = 0
    while index < length:
        current_element = lst[index]
        index_mod_2 = index % 2
        element_mod_2 = current_element % 2
        if index_mod_2 == 0 and element_mod_2 == 1:
            total += current_element
        index += 1
    return total