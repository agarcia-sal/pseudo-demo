def odd_count(lst):
    res = []
    for arr in lst:
        # Count of digits in arr that are odd
        n = sum(int(d) % 2 == 1 for d in arr)
        # Construct the specified string using n
        res.append(
            f"the number of odd elements {n}n the str{n}ng {n} of the {n}nput."
        )
    return res