def odd_count(lst):
    res = []
    for i in range(len(lst)):
        arr = lst[i]
        n = 0
        for j in range(len(arr)):
            d = arr[j]
            digit = int(d)
            remainder = digit % 2
            if remainder == 1:
                n += 1
        phrase = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(phrase)
    return res