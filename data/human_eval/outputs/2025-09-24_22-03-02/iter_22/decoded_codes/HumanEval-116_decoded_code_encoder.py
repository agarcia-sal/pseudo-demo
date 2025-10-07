from functools import cmp_to_key

def sort_array(arr):
    def convert_to_binary_string_without_prefix(num):
        abs_num = -num if num < 0 else num
        if abs_num == 0:
            return "0"
        binary_string = ""
        while abs_num > 0:
            remainder = abs_num % 2
            abs_num //= 2
            binary_string = str(remainder) + binary_string
        return binary_string

    def count_character_in_string(string, character):
        count = 0
        i = 0
        while i < len(string):
            if string[i] == character:
                count += 1
            i += 1
        return count

    def compare_function(x, y):
        bin_x = convert_to_binary_string_without_prefix(x)
        count_ones_x = count_character_in_string(bin_x, '1')
        bin_y = convert_to_binary_string_without_prefix(y)
        count_ones_y = count_character_in_string(bin_y, '1')
        if count_ones_x < count_ones_y:
            return -1
        elif count_ones_x == count_ones_y:
            return -1 if x < y else (1 if x > y else 0)
        else:
            return 1

    arr.sort(key=cmp_to_key(compare_function))
    return arr