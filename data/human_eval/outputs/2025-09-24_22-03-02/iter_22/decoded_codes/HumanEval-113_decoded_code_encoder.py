def odd_count(lst):
    res = []
    for index in range(len(lst)):
        arr = lst[index]
        n = 0
        for digit_index in range(len(arr)):
            d = arr[digit_index]
            d_int = int(d)
            d_mod = d_int % 2
            if d_mod == 1:
                n += 1
        str_n = str(n)
        out_string = "the number of odd elements " + str_n + "n the str" + str_n + "ng " + str_n + " of the " + str_n + "nput."
        res.append(out_string)
    return res