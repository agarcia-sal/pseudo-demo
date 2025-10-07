def odd_count(lst):
    res = []
    for index_i in range(len(lst)):
        arr = lst[index_i]
        n = 0
        for index_j in range(len(arr)):
            d = arr[index_j]
            d_int = int(d)
            if d_int % 2 == 1:
                n += 1
        str_n = str(n)
        phrase = "the number of odd elements " + str_n + "n the str" + str_n + "ng " + str_n + " of the " + str_n + "nput."
        res.append(phrase)
    return res