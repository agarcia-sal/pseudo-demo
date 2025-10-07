class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        chars_count = {}
        idx_x = 0
        while idx_x < len(word):
            curr_char = word[idx_x]
            if curr_char not in chars_count:
                chars_count[curr_char] = 1
            else:
                chars_count[curr_char] += 1
            idx_x += 1

        freq_list = []
        for val_c in chars_count:
            freq_list.append(chars_count[val_c])

        freq_list = self.sortAscending(freq_list)

        min_del = 10 ** 20

        def tailRecursiveLoop(idx_i, current_min):
            if idx_i > len(freq_list) - 1:
                return current_min

            max_freq_allowed = freq_list[idx_i] + k
            delete_sum = 0

            inner_pos = idx_i + 1
            while inner_pos <= len(freq_list) - 1:
                if freq_list[inner_pos] > max_freq_allowed:
                    delete_sum += freq_list[inner_pos] - max_freq_allowed
                inner_pos += 1

            pre_pos = 0
            while pre_pos < idx_i:
                delete_sum += freq_list[pre_pos]
                pre_pos += 1

            if delete_sum < current_min:
                current_min = delete_sum

            return tailRecursiveLoop(idx_i + 1, current_min)

        min_del = tailRecursiveLoop(0, min_del)
        return min_del

    def sortAscending(self, arr):
        if len(arr) <= 1:
            return arr
        pivot_idx = len(arr) // 2
        pivot_val = arr[pivot_idx]
        left_bucket = []
        right_bucket = []
        middle_bucket = []

        pos = 0
        while pos < len(arr):
            if arr[pos] < pivot_val:
                left_bucket.append(arr[pos])
            elif arr[pos] > pivot_val:
                right_bucket.append(arr[pos])
            else:
                middle_bucket.append(arr[pos])
            pos += 1

        return self.concatenateLists(
            self.sortAscending(left_bucket),
            middle_bucket,
            self.sortAscending(right_bucket)
        )

    def concatenateLists(self, list_a, list_b, list_c):
        res = []
        for element in list_a:
            res.append(element)
        for element in list_b:
            res.append(element)
        for element in list_c:
            res.append(element)
        return res