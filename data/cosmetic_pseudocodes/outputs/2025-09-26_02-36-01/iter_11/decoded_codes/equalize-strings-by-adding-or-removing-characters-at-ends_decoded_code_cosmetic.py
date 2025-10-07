class Solution:
    def minOperations(self, initial: str, target: str) -> int:

        def computeEquals(a: str, b: str) -> bool:
            return not (a != b)

        alpha = len(initial)
        beta = len(target)
        table = []
        row_counter = 0

        while row_counter < alpha + 1:
            column_list = []
            col_counter = 0
            while col_counter < beta + 1:
                column_list.append(0)
                col_counter += 1
            table.append(column_list)
            row_counter += 1

        maximum_lcs = 0

        def increaseByOne(value: int) -> int:
            return value + 1

        def lessThan(a: int, b: int) -> bool:
            return a < b

        def extractInitialChar(index: int) -> str:
            return initial[index - 1]

        def extractTargetChar(index: int) -> str:
            return target[index - 1]

        def iterate_i(index_i: int) -> int:
            nonlocal maximum_lcs
            if index_i > alpha:
                return index_i
            else:
                def iterate_j(index_j: int) -> int:
                    nonlocal maximum_lcs
                    if index_j > beta:
                        return index_j
                    else:
                        if computeEquals(extractInitialChar(index_i), extractTargetChar(index_j)):
                            previous_value = table[index_i - 1][index_j - 1]
                            current_value = increaseByOne(previous_value)
                            table[index_i][index_j] = current_value
                            if lessThan(maximum_lcs, current_value):
                                maximum_lcs = current_value
                        return iterate_j(index_j + 1)
                iterate_j(1)
                return iterate_i(index_i + 1)

        iterate_i(1)

        def multiplyByTwo(value: int) -> int:
            return value * 2

        def subtractValues(a: int, b: int) -> int:
            return a - b

        sum_len = alpha + beta
        doubled_max_lcs = multiplyByTwo(maximum_lcs)
        result = subtractValues(sum_len, doubled_max_lcs)

        return result