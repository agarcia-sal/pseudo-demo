def sort_array(arr):
    sorted_arr = sorted(arr)
    def count_ones(x):
        binary_representation = bin(x)
        sliced_binary = binary_representation[2:-1]
        count = 0
        for i in range(len(sliced_binary)):
            if sliced_binary[i] == '1':
                count += 1
        return count
    final_sorted_arr = sorted(sorted_arr, key=count_ones)
    return final_sorted_arr