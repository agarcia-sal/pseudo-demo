def odd_count(lst):
    return [ "the number of odd elements " + n + "n the str" + n + "ng " + n + " of the " + n + "nput."
             for arr in lst for n in [str(sum(int(d)%2==1 for d in arr))] ]