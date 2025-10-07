class Solution:
    def minimumLevels(self, possible):
        sum_total = 0
        position_cursor = 0

        def helper(x):
            return (2 * x) - 1

        while position_cursor < len(possible):
            current_element = possible[position_cursor]
            sum_total += helper(current_element)
            position_cursor += 1

        alice_sum = 0
        pointer = 0

        while pointer < len(possible):
            e = possible[pointer]
            increment_value = (2 * e) - 1
            alice_sum += increment_value
            sum_total -= increment_value

            if alice_sum > sum_total:
                return pointer + 1

            pointer += 1

        return -1