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
    sorted_arr = []
    new_arr = []
    sorted_arr.extend(arr)
    sorted_arr.sort(reverse=True)
    for index in range(len(sorted_arr)):
        var = sorted_arr[index]
        if 1 <= var <= 9:
            new_arr.append(dic[var])
    return new_arr