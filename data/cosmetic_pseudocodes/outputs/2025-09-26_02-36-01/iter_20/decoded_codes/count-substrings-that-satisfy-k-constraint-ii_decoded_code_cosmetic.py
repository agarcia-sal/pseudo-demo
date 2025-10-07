class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:
        w = len(s) + 1
        X = [0] * w  # prefix sums of zeros
        Y = [0] * w  # prefix sums of ones

        def accumulate_counts():
            a = 0
            while a < w - 1:
                b = a + 1
                p = X[a] + (1 if s[a] == '0' else 0)
                X[b] = p
                q = Y[a] + (1 if s[a] == '1' else 0)
                Y[b] = q
                a = b

        accumulate_counts()

        def count_valid_substrings(l: int, r: int) -> int:
            total = 0
            start_index = l

            while start_index <= r:
                def binary_search(left: int, right: int) -> int:
                    if left >= right:
                        return left
                    middle = (left + right) // 2
                    zero_subcount = X[middle + 1] - X[start_index]
                    one_subcount = Y[middle + 1] - Y[start_index]
                    if zero_subcount <= k or one_subcount <= k:
                        return binary_search(middle + 1, right)
                    else:
                        return binary_search(left, middle)

                upper_bound = r + 1
                pos = binary_search(start_index, upper_bound) - 1
                if pos >= start_index:
                    total += (pos - start_index + 1)
                start_index += 1

            return total

        output = []
        qidx = 0
        while qidx < len(queries):
            pair = queries[qidx]
            left_bound = pair[0]
            right_bound = pair[1]
            output.append(count_valid_substrings(left_bound, right_bound))
            qidx += 1

        return output