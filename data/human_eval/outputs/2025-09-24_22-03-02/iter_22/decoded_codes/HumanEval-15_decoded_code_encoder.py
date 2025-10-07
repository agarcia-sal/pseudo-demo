def string_sequence(n: int) -> str:
    result = ""
    i = 0
    while i <= n:
        if i == 0:
            result = str(i)
        else:
            result += " " + str(i)
        i += 1
    return result