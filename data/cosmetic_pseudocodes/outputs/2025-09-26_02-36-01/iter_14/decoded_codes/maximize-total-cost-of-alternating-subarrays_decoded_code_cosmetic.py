class Solution:
    def maximumTotalCost(self, nums):
        count = len(nums)
        if count <= 1:
            return nums[0]

        cache = [0] * count
        cache[count - 1] = nums[count - 1]

        for index in range(count - 2, -1, -1):
            acc = nums[index]

            if acc > cache[index + 1]:
                cache[index] = acc
            else:
                cache[index] = cache[index + 1] + acc

            inner = index + 1
            while inner < count:
                sign = (-1) ** (inner - index)
                acc += nums[inner] * sign

                if inner + 1 < count:
                    if cache[index] < acc + cache[inner + 1]:
                        cache[index] = acc + cache[inner + 1]
                else:
                    if cache[index] < acc:
                        cache[index] = acc

                inner += 1

        return cache[0]