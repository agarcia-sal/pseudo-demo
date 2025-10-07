def odd_count(lst):
    res = []
    for arr in lst:
        n = 0
        for d in arr:
            digit_value = int(d)
            if digit_value % 2 == 1:
                n += 1
        n_str = str(n)
        constructed_string = "the number of odd elements " + n_str + "n the str" + n_str + "ng " + n_str + " of the " + n_str + "nput."
        res.append(constructed_string)
    return res