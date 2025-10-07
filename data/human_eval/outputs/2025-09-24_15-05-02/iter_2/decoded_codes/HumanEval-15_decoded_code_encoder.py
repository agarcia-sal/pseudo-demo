def string_sequence(n: int) -> str:
    list_of_strings = []
    for x in range(n + 1):
        list_of_strings.append(str(x))
    return " ".join(list_of_strings)