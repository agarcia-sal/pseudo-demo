def odd_count(lst):
    res = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        string_part = f"the number of odd elements {n}n the str{n}ng {n} of the {n}nput."
        res.append(string_part)
    return res