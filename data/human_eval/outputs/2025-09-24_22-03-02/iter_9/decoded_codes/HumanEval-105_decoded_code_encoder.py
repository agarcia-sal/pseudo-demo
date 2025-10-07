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
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    filtered_arr.sort(reverse=True)
    new_arr = [dic[var] for var in filtered_arr]
    return new_arr