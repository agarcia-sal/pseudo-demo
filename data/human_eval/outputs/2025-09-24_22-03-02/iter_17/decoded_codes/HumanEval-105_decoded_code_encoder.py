def by_length(arr):
    dic = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    sorted_arr = sorted(arr, reverse=True)
    new_arr = [dic[var] for var in sorted_arr if 1 <= var <= 9]
    return new_arr