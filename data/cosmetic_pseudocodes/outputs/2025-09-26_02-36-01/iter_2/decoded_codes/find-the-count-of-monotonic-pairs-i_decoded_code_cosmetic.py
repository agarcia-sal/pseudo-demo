class Solution:
    def countOfPairs(self, nums):
        modulus = 10**9 + 7
        length = len(nums)
        highest = max(nums)

        # Initialize 3D dp_table with dimensions: length x (highest+1) x (highest+1)
        dp_table = [[[0] * (highest + 1) for _ in range(highest + 1)] for _ in range(length)]

        first_val = nums[0]
        x = 0
        while x <= first_val:
            y = first_val - x
            dp_table[0][x][y] = 1
            x += 1

        index = 1
        while index < length:
            current_val = nums[index]
            x_curr = 0
            while x_curr <= current_val:
                y_curr = current_val - x_curr
                x_prev = 0
                while x_prev <= x_curr:
                    y_prev = y_curr
                    while y_prev <= highest:
                        dp_table[index][x_curr][y_curr] = (dp_table[index][x_curr][y_curr] + dp_table[index - 1][x_prev][y_prev]) % modulus
                        y_prev += 1
                    x_prev += 1
                x_curr += 1
            index += 1

        total = 0
        val1 = 0
        last_num = nums[-1]
        while val1 <= highest:
            val2 = 0
            while val2 <= highest:
                if val1 + val2 == last_num:
                    total = (total + dp_table[length - 1][val1][val2]) % modulus
                val2 += 1
            val1 += 1

        return total