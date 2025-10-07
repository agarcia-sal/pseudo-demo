from collections import defaultdict
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def calc(arr: List[int]) -> int:
            m = len(arr)
            alpha = [0] * m
            beta = [0] * m

            def makeCounter():
                return defaultdict(int)

            delta = makeCounter()

            def forwardPass():
                idx = 1
                while idx < m:
                    val1 = arr[idx - 1]
                    currentCount = delta[val1]
                    delta[val1] = currentCount + 1
                    alpha[idx] = delta[val1] - 1
                    idx += 1

            forwardPass()

            delta = makeCounter()

            def backwardPass():
                idx = m - 2
                while idx >= 0:
                    val2 = arr[idx + 1]
                    delta[val2] += 1
                    beta[idx] = delta[val2]
                    idx -= 1

            backwardPass()

            accumulator = 0

            def accumulateSum():
                nonlocal accumulator
                p = 0
                while p < m:
                    u = alpha[p]
                    v = beta[p]
                    w = arr[p]
                    subtotal = (u + v + u * v) * w
                    accumulator += subtotal
                    p += 1

            accumulateSum()

            return accumulator % MOD

        firstPass = calc(nums)

        def reverseList(lst: List[int]) -> None:
            start, end = 0, len(lst) - 1
            while start < end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1

        reverseList(nums)

        secondPass = calc(nums)

        totalSum = (firstPass + secondPass + sum(nums)) % MOD
        return totalSum