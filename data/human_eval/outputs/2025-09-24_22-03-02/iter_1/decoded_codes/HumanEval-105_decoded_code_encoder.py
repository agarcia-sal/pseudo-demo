def map_numbers(arr):
    dic = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
    filtered = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(filtered)
    reversed_arr = sorted_arr[::-1]
    return [dic[x] for x in reversed_arr]