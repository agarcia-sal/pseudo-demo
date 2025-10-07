def digitSum(text_var: str) -> int:
    counter_var = 0
    index_var = 0
    while index_var < len(text_var):
        char = text_var[index_var]
        if not (char < "A" or char > "Z"):
            counter_var += ord(char)
        index_var += 1
    return counter_var