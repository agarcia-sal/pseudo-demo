def odd_count(lst) -> list:
    res = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        full_string = (
            "the number of odd elements "
            + str(n)
            + "n the str"
            + str(n)
            + "ng "
            + str(n)
            + " of the "
            + str(n)
            + "nput."
        )
        res.append(full_string)
    return res