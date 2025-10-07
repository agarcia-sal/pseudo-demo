def odd_count(lst):
    res = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        constructed_string = f"the number of odd elements {n}n the str{n}ng {n} of the {n}nput."
        res.append(constructed_string)
    return res