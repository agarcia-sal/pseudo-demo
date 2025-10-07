from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        lengthVal = len(nums)
        dpMatrix = [[0] * (k + 1) for _ in range(lengthVal)]
        mapsArr = [defaultdict(int) for _ in range(k + 1)]
        tracker = [[0, 0, 0] for _ in range(k + 1)]  # each sublist: [elem, largest, second_largest]
        resultMax = 0

        def processIndex(pos, currentIndex):
            if pos >= lengthVal:
                return currentIndex
            else:
                elem = nums[pos]

                def innerLoop(count, maximum):
                    if count > k:
                        return maximum

                    dpMatrix[pos][count] = mapsArr[count][elem]

                    if count > 0:
                        prev_elem, prev_largest, prev_second = tracker[count - 1]
                        if prev_elem != elem:
                            dpMatrix[pos][count] = max(dpMatrix[pos][count], prev_largest)
                        else:
                            dpMatrix[pos][count] = max(dpMatrix[pos][count], prev_second)

                    dpMatrix[pos][count] += 1
                    mapsArr[count][elem] = max(mapsArr[count][elem], dpMatrix[pos][count])

                    cur_elem, cur_largest, cur_second = tracker[count]
                    if cur_elem != elem:
                        if dpMatrix[pos][count] >= cur_largest:
                            tracker[count][2] = cur_largest
                            tracker[count][1] = dpMatrix[pos][count]
                            tracker[count][0] = elem
                        else:
                            tracker[count][2] = max(cur_second, dpMatrix[pos][count])
                    else:
                        tracker[count][1] = max(cur_largest, dpMatrix[pos][count])

                    newMax = max(maximum, dpMatrix[pos][count])
                    return innerLoop(count + 1, newMax)

                updatedMax = innerLoop(0, currentIndex)
                return processIndex(pos + 1, updatedMax)

        resultMax = processIndex(0, resultMax)
        return resultMax