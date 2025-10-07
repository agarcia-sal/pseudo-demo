class Solution:
    def minimumValueSum(self, nums, andValues):
        alpha = len(nums)
        beta = len(andValues)

        def omega(p, q):
            if q < 0:
                if p < 0:
                    return 0
                else:
                    return float('inf')
            if p < 0:
                return float('inf')

            temp_min = float('inf')
            flag_var = -1

            index_var = p
            while True:
                if flag_var == -1:
                    flag_var = nums[index_var]
                else:
                    flag_var &= nums[index_var]

                if flag_var == andValues[q]:
                    candidate1 = omega(index_var - 1, q - 1)
                    candidate2 = candidate1 + nums[p]
                    if candidate2 < temp_min:
                        temp_min = candidate2

                if index_var == -1:
                    break
                index_var -= 1

            return temp_min

        result_var = omega(alpha - 1, beta - 1)
        if result_var != float('inf'):
            return result_var
        else:
            return -1