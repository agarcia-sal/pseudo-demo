def odd_count(lst):
    res = []
    for arr in lst:
        n = 0
        for d in arr:
            digit = int(d)
            if digit % 2 == 1:
                n += 1
        part1 = "the number of odd elements " + str(n) + "n the str"
        part2 = str(n) + "ng "
        part3 = str(n) + " of the "
        part4 = str(n) + "nput."
        full_string = part1 + part2 + part3 + part4
        res.append(full_string)
    return res