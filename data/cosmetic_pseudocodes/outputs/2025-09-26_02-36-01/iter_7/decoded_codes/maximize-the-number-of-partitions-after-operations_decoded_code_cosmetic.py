class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            accumulator = 0
            container = set()
            index_tracker = 0
            n = len(s)
            while index_tracker < n:
                elem = s[index_tracker]
                if len(container) < k:
                    container.add(elem)
                else:
                    if elem in container:
                        index_tracker += 1
                        continue
                    else:
                        accumulator += 1
                        container = {elem}
                index_tracker += 1
            if container:
                accumulator += 1
            return accumulator

        collected_maximum = max_partitions(s, k)
        pos_counter = 0
        n = len(s)
        while pos_counter <= n - 1:
            for alpha_iter in range(ord('a'), ord('z') + 1):
                current_letter = chr(alpha_iter)
                if current_letter == s[pos_counter]:
                    continue
                prefix_part = s[:pos_counter]
                suffix_part = s[pos_counter + 1:]
                modified_string = prefix_part + current_letter + suffix_part
                result_temp = max_partitions(modified_string, k)
                if result_temp > collected_maximum:
                    collected_maximum = result_temp
            pos_counter += 1
        return collected_maximum