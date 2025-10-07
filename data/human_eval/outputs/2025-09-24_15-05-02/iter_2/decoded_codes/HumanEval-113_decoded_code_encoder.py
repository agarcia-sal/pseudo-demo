def odd_count(lst):
    res = []
    for arr in lst:
        n = 0
        for d in arr:
            if int(d) % 2 == 1:
                n += 1
        message = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(message)
    return res