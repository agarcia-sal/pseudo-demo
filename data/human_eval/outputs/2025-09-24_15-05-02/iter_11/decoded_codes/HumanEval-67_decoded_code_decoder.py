def fruit_distribution(s, n):
    list_of_numbers = []
    for element in s.split():
        if element.isdigit():
            list_of_numbers.append(int(element))
    return n - sum(list_of_numbers)