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
    filtered_list = [element for element in arr if 1 <= element <= 9]
    sorted_arr = filtered_list[::-1]
    new_arr = [dic[var] for var in sorted_arr]
    return new_arr