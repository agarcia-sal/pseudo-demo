def by_length(arr):
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    sorted_arr = sorted(arr, reverse=True)
    new_arr = []

    for var in sorted_arr:
        if var in dic:
            new_arr.append(dic[var])

    return new_arr