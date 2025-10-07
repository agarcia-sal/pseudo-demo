class Solution:
    def minOperations(self, source: str, destination: str) -> int:
        length_source = len(source)
        length_destination = len(destination)
        table = [[0] * (length_destination + 1) for _ in range(length_source + 1)]
        longest_common_subsequence = 0

        for idx_source in range(1, length_source + 1):
            for idx_destination in range(1, length_destination + 1):
                if source[idx_source - 1] == destination[idx_destination - 1]:
                    previous_value = table[idx_source - 1][idx_destination - 1]
                    table[idx_source][idx_destination] = previous_value + 1
                    if longest_common_subsequence < table[idx_source][idx_destination]:
                        longest_common_subsequence = table[idx_source][idx_destination]

        total_length = length_source + length_destination
        result = total_length - 2 * longest_common_subsequence
        return result