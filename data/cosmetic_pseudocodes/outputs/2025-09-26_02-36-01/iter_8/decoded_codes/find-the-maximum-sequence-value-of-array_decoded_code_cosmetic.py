class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        Limit = 2 ** 7
        CountNums = len(nums)

        # Initialize DP arrays with False
        State = [[[False] * Limit for _ in range(k + 2)] for __ in range(CountNums + 1)]
        State[0][0][0] = True

        for IndexI in range(CountNums):
            for IndexJ in range(k + 1):
                for IndexX in range(Limit):
                    if not State[IndexI][IndexJ][IndexX]:
                        continue
                    # option 1: do not take nums[IndexI]
                    State[IndexI + 1][IndexJ][IndexX] = True
                    # option 2: take nums[IndexI]
                    mergedBits = IndexX | nums[IndexI]
                    State[IndexI + 1][IndexJ + 1][mergedBits] = True

        State2 = [[[False] * Limit for _ in range(k + 2)] for __ in range(CountNums + 1)]
        State2[CountNums][0][0] = True

        for ReverseI in range(CountNums, 0, -1):
            for ReverseJ in range(k + 1):
                for ReverseY in range(Limit):
                    if not State2[ReverseI][ReverseJ][ReverseY]:
                        continue
                    # option 1: do not take nums[ReverseI - 1]
                    State2[ReverseI - 1][ReverseJ][ReverseY] = True
                    # option 2: take nums[ReverseI - 1]
                    combinedBits = ReverseY | nums[ReverseI - 1]
                    State2[ReverseI - 1][ReverseJ + 1][combinedBits] = True

        answer = 0
        for CurrentI in range(k, CountNums - k + 1):
            for CurrentX in range(Limit):
                if not State[CurrentI][k][CurrentX]:
                    continue
                for CurrentY in range(Limit):
                    if not State2[CurrentI][k][CurrentY]:
                        continue
                    candidate = CurrentX ^ CurrentY
                    if answer < candidate:
                        answer = candidate

        return answer