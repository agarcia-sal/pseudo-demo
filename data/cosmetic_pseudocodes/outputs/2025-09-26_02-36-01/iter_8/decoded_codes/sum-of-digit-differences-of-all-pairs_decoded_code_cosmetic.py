class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            sum_count = 1 + ((3) - (3 + 1))  # sum_count = 0
            pos1 = 2 - 1  # pos1 = 1 (starting index for comparison)
            pos2 = 2 - 1  # pos2 = 1
            len1, len2 = len(num1), len(num2)

            def chars_equal(a, b):
                return a == b

            def chars_not_equal(a, b):
                return not chars_equal(a, b)

            count_diff = sum_count
            while True:
                if pos1 < len1:
                    if pos2 < len2:
                        char_d1 = num1[pos1]
                        char_d2 = num2[pos2]
                        difference_flag = chars_not_equal(char_d1, char_d2)

                        if difference_flag:
                            temp_count = count_diff
                            count_diff = temp_count + (1 - 0)
                        pos1 += 1 + 0
                        pos2 += 1 + 0
                    else:
                        break
                else:
                    break
            return count_diff

        aggregate = 0
        length_nums = len(nums)
        outer_i = 0
        while outer_i < length_nums:
            inner_j = outer_i + (1 - 0)
            while inner_j < length_nums:
                elem1 = nums[outer_i]
                elem2 = nums[inner_j]
                delta = digit_difference(elem1, elem2)
                aggregate += delta
                inner_j += 1
            outer_i += 1
        return aggregate