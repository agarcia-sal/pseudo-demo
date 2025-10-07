class Solution:
    def sumDigitDifferences(self, array_input):
        def diffDigits(valA, valB):
            discrepancy = 0
            # Adjust for 0-based indexing in Python
            for pos_x in range(len(valA)):
                if valA[pos_x] != valB[pos_x]:
                    discrepancy += 1
            return discrepancy

        aggregate_result = 0
        length_var = len(array_input)
        outer_idx = 0
        while outer_idx < length_var:
            inner_idx = outer_idx + 1
            while inner_idx < length_var:
                aggregate_result += diffDigits(array_input[outer_idx], array_input[inner_idx])
                inner_idx += 1
            outer_idx += 1
        return aggregate_result