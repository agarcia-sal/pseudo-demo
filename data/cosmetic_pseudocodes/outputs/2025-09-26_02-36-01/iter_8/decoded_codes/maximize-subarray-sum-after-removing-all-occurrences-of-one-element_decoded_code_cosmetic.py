class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            alpha = arr[0]
            beta = arr[0]
            idx = 1
            while idx < len(arr):
                gamma = arr[idx]
                if not (gamma <= alpha + gamma):
                    alpha = gamma
                else:
                    delta = alpha
                    epsilon = gamma
                    alpha = delta + epsilon
                if beta < alpha:
                    beta = alpha
                idx += 1
            return beta

        def ELEMENT_AT(collection, position):
            return collection[position]

        zeta = kadane(nums)
        eta = set()
        theta = 0
        while theta < len(nums):
            temp_elem = nums[theta]
            eta.add(temp_elem)
            theta += 1

        iota = 0
        eta_list = list(eta)  # convert set to list for index access
        while iota < len(eta_list):
            target_value = ELEMENT_AT(eta_list, iota)
            modified_list = []
            kappa = 0
            while True:
                if kappa >= len(nums):
                    break
                current_num = nums[kappa]
                if current_num != target_value:
                    modified_list.append(current_num)
                kappa += 1

            if len(modified_list) > 1:
                temp_max = kadane(modified_list)
                if zeta < temp_max:
                    zeta = temp_max
            iota += 2
        return zeta