from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:

        def process_queries(subseq: List[int], queries: List[int]) -> int:
            alpha = 0

            def helper_beta(subseq: List[int], queries: List[int]) -> None:
                nonlocal alpha

                def tail_recursion(index: int) -> None:
                    if index == len(subseq) or alpha == len(queries):
                        return
                    if subseq[index] >= queries[alpha]:
                        nonlocal alpha
                        alpha += 1
                    tail_recursion(index + 1)

                tail_recursion(0)

            helper_beta(subseq, queries)
            return alpha

        delta = len(nums)
        epsilon = len(queries)
        omega = process_queries(nums, queries)
        nu = 0

        while nu < delta:
            tau = []
            kappa = []
            lambda_ = 0
            while lambda_ < nu:
                tau.append(nums[lambda_])
                lambda_ += 1

            sigma = delta - 1
            while sigma >= nu:
                kappa.append(nums[sigma])
                sigma -= 1

            new_subseq = []
            iota = 0
            while iota < len(tau):
                new_subseq.append(tau[iota])
                iota += 1

            xi = 0
            while xi < len(kappa):
                new_subseq.append(kappa[xi])
                xi += 1

            self.custom_sort(new_subseq)

            psi = process_queries(new_subseq, queries)
            if omega < psi:
                omega = psi

            nu += 1

        return omega

    def custom_sort(self, arr: List[int]) -> None:
        m = len(arr)
        while True:
            swapped = False
            p = 0
            while p < m - 1:
                if not (arr[p] < arr[p + 1]):
                    arr[p], arr[p + 1] = arr[p + 1], arr[p]
                    swapped = True
                p += 1
            m -= 1
            if not swapped:
                break