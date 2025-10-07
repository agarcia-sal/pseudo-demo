from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        def eliminateStale(heap, metrics):
            while heap:
                x = heap[0]
                if -x[0] != metrics[x[1]]:
                    heapq.heappop(heap)
                else:
                    break

        alpha = defaultdict(int)
        omega = []
        sigma = []

        def iterate(i):
            if i < len(nums):
                kappa = nums[i]
                mu = freq[i]
                alpha[kappa] += mu
                beta = -alpha[kappa]
                heapq.heappush(omega, [beta, kappa])
                eliminateStale(omega, alpha)
                if omega:
                    sigma.append(-omega[0][0])
                else:
                    sigma.append(0)
                iterate(i + 1)

        iterate(0)
        return sigma