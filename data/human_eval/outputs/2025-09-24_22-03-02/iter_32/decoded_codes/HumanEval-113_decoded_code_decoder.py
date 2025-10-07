def odd_count(lst):
    res = []
    for i in range(len(lst)):
        arr = lst[i]
        n = 0
        for j in range(len(arr)):
            d = arr[j]
            digit_to_int = int(d)
            is_odd = (digit_to_int % 2 == 1)
            if is_odd:
                n += 1
        n_as_string = str(n)
        part1 = "the number of odd elements " + n_as_string
        part2 = part1 + "n the str"
        part3 = part2 + n_as_string
        part4 = part3 + "ng "
        part5 = part4 + n_as_string
        part6 = part5 + " of the "
        part7 = part6 + n_as_string
        full_string = part7 + "nput."
        res.append(full_string)
    return res