class Solution:
    def minimumPushes(self, word):
        def calculateFrequency(text):
            freq_map = {}
            idx = 0
            while idx < len(text):
                ch = text[idx]
                if ch in freq_map:
                    freq_map[ch] += 1
                else:
                    freq_map[ch] = 1
                idx += 1
            return freq_map

        def extractValues(m):
            return [m[k] for k in m]

        def descendingSort(arr):
            n = len(arr)
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        frequency_map = calculateFrequency(word)
        counts = extractValues(frequency_map)
        ordered_counts = descendingSort(counts)

        accumulated_presses = 0
        presses_per_key = 1
        current_key_count = 0

        def processIndex(i):
            nonlocal accumulated_presses, presses_per_key, current_key_count
            if i >= len(ordered_counts):
                return
            accumulated_presses += ordered_counts[i] * presses_per_key
            current_key_count += 1
            if current_key_count >= 8:
                presses_per_key += 1
                current_key_count = 0
            processIndex(i + 1)

        processIndex(0)
        return accumulated_presses