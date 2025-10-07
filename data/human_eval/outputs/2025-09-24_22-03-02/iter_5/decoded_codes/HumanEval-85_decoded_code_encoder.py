def add(lst) -> int:
    sum_of_elements = 0
    for index in range(1, len(lst), 2):
        if lst[index] % 2 == 0:
            sum_of_elements += lst[index]
    return sum_of_elements