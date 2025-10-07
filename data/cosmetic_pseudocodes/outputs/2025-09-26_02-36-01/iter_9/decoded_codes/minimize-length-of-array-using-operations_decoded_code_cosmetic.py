class Solution:
    def minimumArrayLength(self, input_seq):
        def computeMinValue(sequence):
            current_min = sequence[0]
            index_ptr = 1
            while index_ptr < len(sequence):
                if sequence[index_ptr] < current_min:
                    current_min = sequence[index_ptr]
                index_ptr += 1
            return current_min

        def countOccurrences(sequence, target):
            total_count = 0
            cursor = 0
            while cursor < len(sequence):
                if sequence[cursor] == target:
                    total_count += 1
                cursor += 1
            return total_count

        temp_min = computeMinValue(input_seq)
        freq_min = countOccurrences(input_seq, temp_min)

        if not (freq_min != 1):
            return 1
        else:
            dividend = freq_min + 1
            result_val = dividend / 2
            return result_val