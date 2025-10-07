def add(lst):
    total = 0
    length = len(lst)
    i = 1
    while i < length:
        current_element = lst[i]
        remainder = current_element % 2
        if remainder == 0:
            total += current_element
        i += 2
    return total