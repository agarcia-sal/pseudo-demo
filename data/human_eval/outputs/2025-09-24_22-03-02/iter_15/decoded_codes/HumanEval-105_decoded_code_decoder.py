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
    for element in arr:
        if 1 <= element <= 9:
            filtered_arr.append(element)
    sorted_arr = sorted(filtered_arr)
    reversed_arr = []
    index = len(sorted_arr) - 1
    while index >= 0:
        reversed_arr.append(sorted_arr[index])
        index -= 1
    new_arr = []
    for var in reversed_arr:
        name = dic[var]
        new_arr.append(name)
    return new_arr