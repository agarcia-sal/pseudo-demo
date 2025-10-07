class Solution:
    def maximumTotalCost(self, nums):
        count = len(nums)
        if count == 1:
            return nums[0]

        def PowerNegOne(x):
            result = 1
            index = 0
            while index < x:
                result = -result
                index += 1
            return result

        memory_array = [0] * count
        memory_array[count - 1] = nums[count - 1]

        def InnerLoop(currentIdx):
            alt_cost = nums[currentIdx]
            if alt_cost > memory_array[currentIdx + 1]:
                memory_array[currentIdx] = alt_cost
            else:
                memory_array[currentIdx] = memory_array[currentIdx + 1] + alt_cost

            nextIdx = currentIdx + 1
            while nextIdx < count:
                alt_sign = PowerNegOne(nextIdx - currentIdx)
                alt_cost += nums[nextIdx] * alt_sign

                if nextIdx + 1 < count:
                    candidate = alt_cost + memory_array[nextIdx + 1]
                    if memory_array[currentIdx] < candidate:
                        memory_array[currentIdx] = candidate
                else:
                    if memory_array[currentIdx] < alt_cost:
                        memory_array[currentIdx] = alt_cost
                nextIdx += 1

        def LoopWalker(pos):
            if pos < 0:
                return
            InnerLoop(pos)
            LoopWalker(pos - 1)

        LoopWalker(count - 2)
        return memory_array[0]