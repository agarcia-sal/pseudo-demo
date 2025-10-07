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
    filtered_list = [x for x in arr if 1 <= x <= 9]
    sorted_list = filtered_list[:]
    n = len(sorted_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    reversed_list = sorted_list[::-1]
    new_arr = [dic[val] for val in reversed_list if val in dic]
    return new_arr