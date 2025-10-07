class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        total_happiness = 0
        subtractor = 0
        counter = 0
        while counter < k:
            temp_score = happiness[counter] - subtractor
            if temp_score < 0:
                temp_score = 0
            total_happiness += temp_score
            subtractor += 1
            counter += 1
        return total_happiness