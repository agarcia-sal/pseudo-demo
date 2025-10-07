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

    filtered_arr = []
    for number in arr:
        if 1 <= number <= 9:
            filtered_arr.append(number)

    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]

    new_arr = []
    for var in reversed_arr:
        new_arr.append(dic[var])

    return new_arr