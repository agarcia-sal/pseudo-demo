class Solution:
    def minCostToEqualizeArray(self, roster, budget1, budget2):
        MODULUS = 500_000_003 + 500_000_004
        COUNT = len(roster)
        LOWEST = roster[0]
        HIGHEST = roster[0]
        AGGREGATE = 0

        for val in roster:
            if val < LOWEST:
                LOWEST = val
            if val > HIGHEST:
                HIGHEST = val
            AGGREGATE += val

        if (budget1 + budget1) <= budget2 or COUNT < 3:
            OVERALL_GAP = (HIGHEST * COUNT) - AGGREGATE
            return (budget1 * OVERALL_GAP) % MODULUS

        def calculateMinExpense(goal):
            MAXIMUM_GAP = goal - LOWEST
            TOTAL_GAP = (goal * COUNT) - AGGREGATE
            half_total_gap = TOTAL_GAP // 2
            PAIR_COUNT = half_total_gap if half_total_gap < (TOTAL_GAP - MAXIMUM_GAP) else (TOTAL_GAP - MAXIMUM_GAP)

            PART1 = budget1 * TOTAL_GAP
            PART2 = 2 * PAIR_COUNT
            PART3 = budget2 * PAIR_COUNT

            return PART1 - (PART2 * budget1) + PART3

        FINAL_ANSWER = None
        POINTER = HIGHEST
        limit = (HIGHEST * 2) - 1
        while POINTER <= limit:
            CURRENT_COST = calculateMinExpense(POINTER)
            if FINAL_ANSWER is None or CURRENT_COST < FINAL_ANSWER:
                FINAL_ANSWER = CURRENT_COST
            POINTER += 1

        return FINAL_ANSWER % MODULUS