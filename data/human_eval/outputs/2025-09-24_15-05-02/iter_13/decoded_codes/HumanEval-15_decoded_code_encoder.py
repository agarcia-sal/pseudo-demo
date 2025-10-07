def string_sequence(n):
    list_of_strings = []
    for x in range(n + 1):
        list_of_strings.append(str(x))
    result = " ".join(list_of_strings)
    return result