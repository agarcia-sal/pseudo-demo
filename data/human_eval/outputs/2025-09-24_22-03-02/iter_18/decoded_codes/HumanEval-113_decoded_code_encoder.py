def odd_count(lst):
    res = []
    for index in range(len(lst)):
        arr = lst[index]
        n = 0
        for digit_index in range(len(arr)):
            d = arr[digit_index]
            digit_value = int(d)
            if digit_value % 2 == 1:
                n += 1
        s = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(s)
    return res