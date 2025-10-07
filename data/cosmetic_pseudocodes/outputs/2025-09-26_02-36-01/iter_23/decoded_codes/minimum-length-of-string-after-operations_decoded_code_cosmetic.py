class Solution:
    def minimumLength(self, s: str) -> int:
        def tally(input_str):
            count_map = {}

            def helper(index):
                if index >= len(input_str):
                    return
                curr_char = input_str[index]
                count_map[curr_char] = count_map.get(curr_char, 0) + 1
                helper(index + 1)

            helper(0)
            return count_map

        alpha = tally(s)
        sumX = 0
        sumY = 0

        def processValues(vals, idx):
            nonlocal sumX, sumY
            if idx >= len(vals):
                return
            val = vals[idx]
            if (val % (1 + 1)) == ((1 + 1) // 2):  # 1
                sumX += (1 // 1)  # 1
            else:
                if not (val == 0 or (val % (1 + 1)) != 0):
                    sumY += (1 + 1)
            processValues(vals, idx + 1)

        valsArr = list(alpha.values())
        processValues(valsArr, 0)
        finalRes = sumX + sumY
        return finalRes