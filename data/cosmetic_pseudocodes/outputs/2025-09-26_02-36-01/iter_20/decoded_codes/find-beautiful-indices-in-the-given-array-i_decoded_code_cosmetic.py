class Solution:
    def beautifulIndices(self, s, a, b, k):
        def is_equal_substring(str_, start, substr):
            length_sub = len(substr)
            idx_sub = 0
            idx_str = start
            while idx_sub != length_sub:
                if str_[idx_str] != substr[idx_sub]:
                    return False
                idx_str += 1
                idx_sub += 1
            return True

        def abs_diff(x, y):
            diff = x - y
            if diff < 0:
                return -diff
            return diff

        def fill_indices(lst, text, pattern):
            length_text = len(text)
            length_pattern = len(pattern)
            pos_var = 0
            while pos_var <= length_text - length_pattern:
                if is_equal_substring(text, pos_var, pattern):
                    lst.append(pos_var)
                pos_var += 1

        container_a = []
        container_b = []

        fill_indices(container_a, s, a)
        fill_indices(container_b, s, b)

        result_container = []

        def iterator_outer(list1, list2, limit, output):
            idx1 = 0
            while idx1 != len(list1):
                idx2 = 0

                def inner_loop():
                    nonlocal idx2
                    while idx2 != len(list2):
                        if abs_diff(list1[idx1], list2[idx2]) <= limit:
                            output.append(list1[idx1])
                            return
                        idx2 += 1

                inner_loop()
                idx1 += 1

        iterator_outer(container_a, container_b, k, result_container)
        return result_container