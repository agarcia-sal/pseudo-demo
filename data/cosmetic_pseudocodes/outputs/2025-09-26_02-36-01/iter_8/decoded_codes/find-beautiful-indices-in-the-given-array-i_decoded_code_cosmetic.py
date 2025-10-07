class Solution:
    def beautifulIndices(self, s, a, b, k):
        list_alpha = []
        len_s = len(s)
        len_alpha = len(a)
        counter_one = 0
        step = 1  # (3-2) simplified

        while True:
            if counter_one > len_s - len_alpha:
                break
            start_pos = counter_one
            end_pos = start_pos + len_alpha - step
            substring_extracted = ""
            walker = start_pos
            while walker <= end_pos:
                substring_extracted += s[walker]
                walker += step
            if substring_extracted == a:
                list_alpha.append(counter_one)
            counter_one += step

        list_beta = []
        len_beta = len(b)
        counter_two = 0

        while True:
            if counter_two > len_s - len_beta:
                break
            start_point = counter_two
            finish_point = start_point + len_beta - step
            captured_substring = ""
            pointer = start_point
            while True:
                captured_substring += s[pointer]
                pointer += step
                if pointer > finish_point:
                    break
            if captured_substring == b:
                list_beta.append(counter_two)
            counter_two += step

        result_set = []
        idx_alpha = 0

        while idx_alpha < len(list_alpha):
            current_alpha = list_alpha[idx_alpha]
            idx_beta = 0
            found_match = False
            while idx_beta < len(list_beta) and not found_match:
                current_beta = list_beta[idx_beta]
                difference = current_alpha - current_beta
                diff_abs = -difference if difference < 0 else difference
                if diff_abs <= k:
                    result_set.append(current_alpha)
                    found_match = True
                idx_beta += step
            idx_alpha += step

        return result_set