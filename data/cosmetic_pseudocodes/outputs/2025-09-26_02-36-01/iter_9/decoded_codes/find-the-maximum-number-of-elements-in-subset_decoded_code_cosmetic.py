class Solution:
    def maximumLength(self, numbers):
        frequency_map = {}
        for num in numbers:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        computed_lengths = {}

        def compute_length(value):
            # Base condition: if value not in map or frequency < 1 then return appropriate length
            if value not in frequency_map or frequency_map[value] < 1:
                if value in frequency_map and frequency_map[value] >= 1:
                    return 1
                else:
                    return 0

            if value in computed_lengths:
                return computed_lengths[value]

            squared_value = value * value
            computed_lengths[value] = compute_length(squared_value) + 2
            return computed_lengths[value]

        maximum_length = 1
        all_keys = list(frequency_map.keys())
        index = 0
        while index < len(all_keys):
            key_element = all_keys[index]
            if key_element == 1:
                frequency = frequency_map[key_element]
                # frequency - 1 - ((frequency // 2) * 2)
                adjusted_frequency = frequency - 1 - ((frequency // 2) * 2)
                if adjusted_frequency > maximum_length:
                    maximum_length = adjusted_frequency
            else:
                candidate_length = compute_length(key_element)
                if candidate_length > maximum_length:
                    maximum_length = candidate_length
            index += 1

        return maximum_length