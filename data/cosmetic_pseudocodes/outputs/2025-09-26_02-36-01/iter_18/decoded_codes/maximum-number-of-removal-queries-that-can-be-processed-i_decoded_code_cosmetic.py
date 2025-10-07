from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            alpha = 0
            beta_list = queries
            gamma_list = subseq
            delta_index = 0

            while delta_index < len(gamma_list):
                if len(beta_list) <= alpha:
                    break
                if gamma_list[delta_index] >= beta_list[alpha]:
                    alpha += 1
                delta_index += 1

            return alpha

        def ascending_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            less_than = []
            greater_or_equal = []
            for element in arr[1:]:
                if element < pivot:
                    less_than.append(element)
                else:
                    greater_or_equal.append(element)
            return ascending_sort(less_than) + [pivot] + ascending_sort(greater_or_equal)

        omega = len(nums)
        psi = len(queries)
        rho = process_queries(nums, queries)

        tau = 0
        while tau < omega:
            upsilon = nums[:tau]  # nums[0 to tau-1]
            phi = nums[tau:]      # nums[tau to omega-1]

            # Build chi by appending elements of phi in reverse order
            chi = []
            sigma = len(phi) - 1
            while sigma >= 0:
                chi.append(phi[sigma])
                sigma -= 1

            combined = upsilon + chi
            sorted_combined = ascending_sort(combined)

            temp_max = process_queries(sorted_combined, queries)
            if temp_max > rho:
                rho = temp_max

            tau += 1

        return rho