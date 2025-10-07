def add(lst):
    total = 0
    # Iterate over odd indices in the list (1, 3, 5, ...)
    for index in range(1, len(lst), 2):
        if lst[index] % 2 == 0:  # Check if the element is even
            total += lst[index]
    return total