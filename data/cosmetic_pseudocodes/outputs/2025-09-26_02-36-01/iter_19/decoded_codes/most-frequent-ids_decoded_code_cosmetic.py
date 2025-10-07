from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        alpha = defaultdict(int)
        omega = []
        sigma = []

        for idx in range(len(nums)):
            phi = nums[idx]
            chi = freq[idx]
            tempVal = alpha[phi] + chi
            alpha[phi] = tempVal

            heapq.heappush(omega, (-tempVal, phi))

            while omega and -omega[0][0] != alpha[omega[0][1]]:
                heapq.heappop(omega)

            if not omega:
                sigma.append(0)
            else:
                topElem = omega[0]
                sigma.append(-topElem[0])

        return sigma