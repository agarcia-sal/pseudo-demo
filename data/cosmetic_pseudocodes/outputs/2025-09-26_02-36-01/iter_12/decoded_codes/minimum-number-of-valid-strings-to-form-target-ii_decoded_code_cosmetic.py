class Solution:
    def minValidStrings(self, words, target):
        def custom_substring(s, start_pos, end_pos):
            # Convert 1-based indices to 0-based indices for Python slicing
            # s[start_pos-1:end_pos] includes characters from start_pos to end_pos inclusive
            return s[start_pos - 1:end_pos]

        def custom_min(a, b):
            return a if a < b else b

        prefix_collection = set()
        word_index = 0
        while True:
            if word_index >= len(words):
                break
            current_word = words[word_index]
            upper_bound = len(current_word)
            pos_iter = 1
            while True:
                if pos_iter > upper_bound:
                    break
                extracted_prefix = custom_substring(current_word, 1, pos_iter)
                prefix_collection.add(extracted_prefix)
                pos_iter += 1
            word_index += 1

        target_length = len(target)
        # Initialize dp_array with large number 2^30
        dp_array = [2**30] * (target_length + 1)
        dp_array[0] = 0

        outer_i = 1
        while outer_i <= target_length:
            inner_j = 1
            while inner_j <= outer_i:
                segment = custom_substring(target, inner_j, outer_i)
                if segment in prefix_collection:
                    candidate_value = dp_array[inner_j - 1] + 1
                    dp_array[outer_i] = custom_min(dp_array[outer_i], candidate_value)
                inner_j += 1
            outer_i += 1

        final_answer = dp_array[target_length]
        if final_answer != 2**30:
            return final_answer
        else:
            return -1