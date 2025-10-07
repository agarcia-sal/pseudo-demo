def odd_count(lst):
    res = []
    for i in range(len(lst)):
        arr = lst[i]
        n = 0
        for j in range(len(arr)):
            d = arr[j]
            digit_value = int(d)
            digit_modulo = digit_value % 2
            if digit_modulo == 1:
                n += 1
        part1 = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(part1)
    return res