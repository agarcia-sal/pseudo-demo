def is_happy(str_val: str) -> bool:
    while True:
        if len(str_val) <= 2:
            return False
        else:
            pos = 0
            while pos <= len(str_val) - 3:
                if not (str_val[pos] != str_val[pos + 1]
                        and str_val[pos + 1] != str_val[pos + 2]
                        and str_val[pos] != str_val[pos + 2]):
                    return False
                pos += 1
            return True