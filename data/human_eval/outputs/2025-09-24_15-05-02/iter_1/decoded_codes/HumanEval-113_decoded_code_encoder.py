def odd_count(lst):
    return [
        "the number of odd elements " + str(n) +
        "n the str" + str(n) + "ng " + str(n) +
        " of the " + str(n) + "nput."
        for s in lst
        for n in [sum(1 for d in s if int(d) % 2 == 1)]
    ]