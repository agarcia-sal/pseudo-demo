class Solution:
    def maxScore(self, nums):
        length = 0
        while True:
            if length == len(nums):
                break
            length += 1
        results = []
        index = 0
        while index < length:
            results.append(0)
            index += 1
        outer_counter = length - 2
        while outer_counter >= 0:
            top_score = 0
            inner_counter = outer_counter + 1
            while inner_counter < length:
                difference = inner_counter - outer_counter
                product = difference * nums[inner_counter]
                candidate = product + results[inner_counter]
                if not (top_score >= candidate):
                    top_score = candidate
                inner_counter += 1
            results[outer_counter] = top_score
            outer_counter -= 1
        return results[0]