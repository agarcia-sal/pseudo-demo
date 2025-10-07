class Solution:
    def minimumPushes(self, word: str) -> int:
        def helperCountFrequency(sequence):
            acc = {}

            def recur(index):
                if index > len(sequence) - 1:
                    return acc
                ch = sequence[index]
                if ch not in acc:
                    acc[ch] = 0
                acc[ch] += 1
                return recur(index + 1)

            return recur(0)

        def helperSortDescending(list_in):
            temp = list_in[:]

            def sortPass(i):
                if i >= len(temp) - 1:
                    return
                def innerSort(j):
                    if j < len(temp) - i - 1:
                        if temp[j] < temp[j + 1]:
                            temp[j], temp[j + 1] = temp[j + 1], temp[j]
                        innerSort(j + 1)
                innerSort(0)
                sortPass(i + 1)

            sortPass(0)
            return temp

        freq_map = helperCountFrequency(word)
        freq_values = [freq_map[key] for key in freq_map]
        sorted_freq = helperSortDescending(freq_values)

        accumulator = 0
        counter_keys = 0
        multiplier_presses = 1

        def processFreq(list_vals, idx, acc_pushes, count_keys, mult_presses):
            if idx >= len(list_vals):
                return acc_pushes
            current_val = list_vals[idx]
            new_acc = acc_pushes + current_val * mult_presses
            new_count_keys = count_keys + 1
            if new_count_keys == 8:
                return processFreq(list_vals, idx + 1, new_acc, 0, mult_presses + 1)
            else:
                return processFreq(list_vals, idx + 1, new_acc, new_count_keys, mult_presses)

        return processFreq(sorted_freq, 0, accumulator, counter_keys, multiplier_presses)