def odd_count(lst) -> list:
    res = []
    for i in range(len(lst)):
        arr = lst[i]
        n = 0
        for j in range(len(arr)):
            d = arr[j]
            if int(d) % 2 == 1:
                n += 1
        s = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(s)
    return res