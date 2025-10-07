from typing import List

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        P = 1 << 7
        totalNums = len(nums)

        # dpForward[i][taken][state] indicates whether it's possible to pick 'taken' numbers 
        # among the first i elements to achieve a bitwise OR = state
        dpForward = [[[False] * P for _ in range(k + 2)] for __ in range(totalNums + 1)]
        dpForward[0][0][0] = True

        def iterateForward(index: int):
            if index == totalNums:
                return
            for taken in range(k + 1):
                dpf_i = dpForward[index][taken]
                dpf_i1 = dpForward[index + 1][taken]
                for state in range(P):
                    if dpf_i[state]:
                        # Not pick current element
                        if not dpForward[index + 1][taken][state]:
                            dpForward[index + 1][taken][state] = True
                        # Pick current element, if possible
                        if taken + 1 <= k + 1:
                            newState = state | nums[index]
                            if not dpForward[index + 1][taken + 1][newState]:
                                dpForward[index + 1][taken + 1][newState] = True
            iterateForward(index + 1)
        iterateForward(0)

        # dpBackward[pos][taken][state] indicates whether it's possible to pick 'taken' numbers 
        # among the elements from pos to end to achieve a bitwise OR = state
        dpBackward = [[[False] * P for _ in range(k + 2)] for __ in range(totalNums + 1)]
        dpBackward[totalNums][0][0] = True

        def iterateBackward(position: int):
            if position == 0:
                return
            posMinusOne = position - 1
            for taken in range(k + 1):
                dpb_pos = dpBackward[position][taken]
                for state in range(P):
                    if dpb_pos[state]:
                        # Not pick element at posMinusOne
                        if not dpBackward[posMinusOne][taken][state]:
                            dpBackward[posMinusOne][taken][state] = True
                        # Pick element at posMinusOne
                        if taken + 1 <= k + 1:
                            newState = state | nums[posMinusOne]
                            if not dpBackward[posMinusOne][taken + 1][newState]:
                                dpBackward[posMinusOne][taken + 1][newState] = True
            iterateBackward(posMinusOne)
        iterateBackward(totalNums)

        result = 0
        # Iterate over all possible split points where k elements are taken on each side
        for index in range(k, totalNums - k + 1):
            dpF_k = dpForward[index][k]
            dpB_k = dpBackward[index][k]
            for fstState in range(P):
                if dpF_k[fstState]:
                    for sndState in range(P):
                        if dpB_k[sndState]:
                            candidate = fstState ^ sndState
                            if candidate > result:
                                result = candidate
        return result