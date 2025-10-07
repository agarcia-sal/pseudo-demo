from typing import List

def sort_array(list_of_numbers: List[int]) -> List[int]:
    def count_ones_in_binary(num: int) -> int:
        binary_string = ""
        temp = num
        while temp > 0:
            remainder = temp % 2
            binary_string = str(remainder) + binary_string
            temp //= 2
        count_ones = sum(1 for char in binary_string if char == '1')
        return count_ones

    def sort_ascending_recursively(input_list: List[int], acc: List[int]) -> List[int]:
        if not input_list:
            return acc
        smallest = input_list[0]
        for val in input_list:
            if val < smallest:
                smallest = val
        filtered_list = [val for val in input_list if val != smallest]
        acc.append(smallest)
        return sort_ascending_recursively(filtered_list, acc)

    ascending_sorted_list = sort_ascending_recursively(list_of_numbers, [])

    def insertion_sort_by_ones_count(arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key_element = arr[i]
            ones_key = count_ones_in_binary(key_element)
            j = i - 1
            while j >= 0 and count_ones_in_binary(arr[j]) > ones_key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_element
        return arr

    sorted_by_ones = insertion_sort_by_ones_count(ascending_sorted_list)
    return sorted_by_ones