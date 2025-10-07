def add(lst) -> int:
    total = 0
    index = 1
    while index < len(lst):
        current_element = lst[index]
        if current_element % 2 == 0:
            total += current_element
        index += 2
    return total