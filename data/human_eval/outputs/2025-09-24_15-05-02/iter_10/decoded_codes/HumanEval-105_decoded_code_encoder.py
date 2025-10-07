def by_length(arr):
    dic = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
    filtered_list = [element for element in arr if 1 <= element <= 9]
    filtered_list.sort()
    filtered_list.reverse()
    new_arr = [dic[var] for var in filtered_list]
    return new_arr