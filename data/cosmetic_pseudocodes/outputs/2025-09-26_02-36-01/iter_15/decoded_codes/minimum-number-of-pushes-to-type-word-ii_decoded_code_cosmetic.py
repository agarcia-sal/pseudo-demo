class Solution:
    def minimumPushes(self, word: str) -> int:
        def tallyFrequency(input_str, output_dict):
            idx = 0
            while idx < len(input_str):
                ch = input_str[idx]
                if ch in output_dict:
                    output_dict[ch] += 1
                else:
                    output_dict[ch] = 1
                idx += 1

        frequency_map = {}
        tallyFrequency(word, frequency_map)

        frequency_values = list(frequency_map.values())

        # Sort frequencies in descending order using an efficient method
        frequency_values.sort(reverse=True)

        acc_pushes = 0
        presses_per_key = 1
        keys_allocated = 0

        k = 0
        while True:
            if k >= len(frequency_values):
                break

            current_freq = frequency_values[k]
            acc_pushes += current_freq * presses_per_key
            keys_allocated += 1

            if keys_allocated == 8:
                keys_allocated = 0
                presses_per_key += 1

            k += 1

        return acc_pushes