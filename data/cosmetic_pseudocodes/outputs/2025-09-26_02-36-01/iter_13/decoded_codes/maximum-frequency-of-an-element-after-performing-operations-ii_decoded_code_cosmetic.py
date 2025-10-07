class Solution:
    def maxFrequency(self, nums, k, numOperations):
        def make_default_map():
            return {}

        map_a = make_default_map()
        map_b = make_default_map()

        def get_map_value(m, key):
            return m[key] if key in m else 0

        def increment_map(m, key, delta):
            current = get_map_value(m, key)
            m[key] = current + delta

        def keys_of_map(m):
            keys_list = []
            for key in m:
                keys_list.append(key)
            return keys_list

        def sorted_items(m):
            s_keys = keys_of_map(m)
            # Bubble sort as per pseudocode
            for i in range(len(s_keys) - 1):
                for j in range(len(s_keys) - 1 - i):
                    if s_keys[j] > s_keys[j + 1]:
                        s_keys[j], s_keys[j + 1] = s_keys[j + 1], s_keys[j]
            result = []
            for each_key in s_keys:
                result.append((each_key, get_map_value(m, each_key)))
            return result

        def process_nums(index):
            if index >= len(nums):
                return
            val = nums[index]
            increment_map(map_a, val, 1)
            increment_map(map_b, val, 0)
            increment_map(map_b, val - k, 1)
            increment_map(map_b, val + k + 1, -1)
            process_nums(index + 1)

        process_nums(0)

        result = 0
        sum_accum = 0

        for key_value, count_value in sorted_items(map_b):
            sum_accum += count_value
            val_in_map_a = get_map_value(map_a, key_value)
            current = min(sum_accum, val_in_map_a + numOperations)
            if result < current:
                result = current

        return result