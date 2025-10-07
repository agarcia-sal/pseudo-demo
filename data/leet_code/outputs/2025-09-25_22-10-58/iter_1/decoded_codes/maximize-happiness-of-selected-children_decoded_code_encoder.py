class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        max_sum = 0
        decrement = 0
        for i in range(k):
            current_value = happiness[i] - decrement
            if current_value < 0:
                current_value = 0
            max_sum += current_value
            decrement += 1
        return max_sum