class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        alpha = len(initial)
        beta = len(target)

        table = []
        p1 = 0
        while p1 <= alpha:
            row = []
            p2 = 0
            while p2 <= beta:
                row.append(0)
                p2 += 1
            table.append(row)
            p1 += 1

        longest = 0

        idx1 = 1
        while idx1 <= alpha:
            idx2 = 1
            while idx2 <= beta:
                if initial[idx1 - 1] == target[idx2 - 1]:
                    table_element = table[idx1 - 1][idx2 - 1] + 1
                    table[idx1][idx2] = table_element
                    if longest < table_element:
                        longest = table_element
                idx2 += 1
            idx1 += 1

        return alpha + beta - 2 * longest