class Solution:
    def maximumTotalCost(self, nums):
        totalCount = len(nums)
        if totalCount == 1:
            return nums[0]
        else:
            table = [0] * totalCount
            indexLast = totalCount - 1
            table[indexLast] = nums[indexLast]

            def recurProcess(position):
                if position < 0:
                    return
                baseVal = nums[position]
                if baseVal > table[position + 1]:
                    table[position] = baseVal
                else:
                    table[position] = baseVal + table[position + 1]

                offset = position + 1
                while offset < totalCount:
                    powerDiff = offset - position
                    signValue = (-1) ** powerDiff
                    baseVal += nums[offset] * signValue
                    if offset + 1 < totalCount:
                        if table[position] < baseVal + table[offset + 1]:
                            table[position] = baseVal + table[offset + 1]
                    else:
                        if table[position] < baseVal:
                            table[position] = baseVal
                    offset += 1

                recurProcess(position - 1)

            recurProcess(indexLast - 1)
            return table[0]