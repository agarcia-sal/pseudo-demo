from collections import defaultdict
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        modulus = 10**9 + 7

        def calc(nums: List[int]) -> int:
            a = len(nums)
            b = [0] * a
            c = [0] * a
            d = defaultdict(int)

            e = 1
            while e < a:
                f = nums[e - 1]
                prev_count = d[f]
                d[f] = prev_count + 1
                b[e] = d[f]
                e += 1

            d = defaultdict(int)

            g = a - 2
            while True:
                if g < 0:
                    break
                h = nums[g + 1]
                prev_val = d[h]
                d[h] = prev_val + 1
                c[g] = d[h]
                g -= 1

            total = 0
            index = 0
            while index < a:
                left_val = b[index]
                right_val = c[index]
                num_val = nums[index]
                partial = (left_val + right_val + (left_val * right_val)) * num_val
                total += partial
                index += 1
            return total % modulus

        varA = calc(nums)

        if len(nums) > 1:
            temp1 = nums.pop()
            nums.insert(0, temp1)

        varB = calc(nums)

        sumAll = sum(nums)

        return (varA + varB + sumAll) % modulus