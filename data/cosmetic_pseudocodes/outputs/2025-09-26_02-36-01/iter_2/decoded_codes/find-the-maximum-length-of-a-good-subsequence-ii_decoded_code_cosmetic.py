from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        lengthNums = len(nums)
        # dp[count] is a dict: key = currentVal, value = max length
        dp = [{} for _ in range(k + 1)]
        # tracker[count] = [val_with_max_length, max_length, second_max_length]
        tracker = [[0, 0, 0] for _ in range(k + 1)]
        maxResult = 0

        for index in range(lengthNums):
            currentVal = nums[index]
            for count in range(k + 1):
                currentDPval = dp[count].get(currentVal, 0)
                if count > 0:
                    if index == 0 or tracker[count][0] != nums[index - 1]:
                        currentDPval = max(currentDPval, tracker[count - 1][1])
                    else:
                        currentDPval = max(currentDPval, tracker[count - 1][2])
                currentDPvalUpdated = currentDPval + 1
                dp[count][currentVal] = max(dp[count].get(currentVal, 0), currentDPvalUpdated)

                if tracker[count][0] != currentVal:
                    if currentDPvalUpdated >= tracker[count][1]:
                        tracker[count][2] = tracker[count][1]
                        tracker[count][1] = currentDPvalUpdated
                        tracker[count][0] = currentVal
                    else:
                        tracker[count][2] = max(tracker[count][2], currentDPvalUpdated)
                else:
                    tracker[count][1] = max(tracker[count][1], currentDPvalUpdated)

                if currentDPvalUpdated > maxResult:
                    maxResult = currentDPvalUpdated

        return maxResult