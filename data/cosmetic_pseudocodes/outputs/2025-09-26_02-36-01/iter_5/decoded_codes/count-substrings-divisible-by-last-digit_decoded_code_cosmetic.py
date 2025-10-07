class Solution:
    def countSubstrings(self, s: str) -> int:
        length_of_s = len(s)

        def process_j(start_index: int, current_pos: int, acc_number: int) -> int:
            if current_pos >= length_of_s:
                return 0
            digit_value = int(s[current_pos])
            updated_number = acc_number * 10 + digit_value
            increment = 0
            if digit_value != 0 and updated_number % digit_value == 0:
                increment = 1
            return increment + process_j(start_index, current_pos + 1, updated_number)

        def iterate_i(index: int) -> int:
            if index >= length_of_s:
                return 0
            subtotal = process_j(index, index, 0)
            return subtotal + iterate_i(index + 1)

        result = iterate_i(0)
        return result