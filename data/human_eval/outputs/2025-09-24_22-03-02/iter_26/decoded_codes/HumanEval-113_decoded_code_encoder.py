def odd_count(lst):
    res = []
    for arr in lst:
        n = 0
        for d in arr:
            digit_value = int(d)
            remainder = digit_value % 2
            if remainder == 1:
                n += 1
        str_n = str(n)
        constructed_string = (
            "the number of odd elements " + str_n +
            "n the str" + str_n +
            "ng " + str_n +
            " of the " + str_n +
            "nput."
        )
        res.append(constructed_string)
    return res