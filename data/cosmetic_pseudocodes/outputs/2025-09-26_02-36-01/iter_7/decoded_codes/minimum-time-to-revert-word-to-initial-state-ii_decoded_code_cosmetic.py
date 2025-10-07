class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        total_length = len(word)
        index_tracker = 1
        while True:
            slice_start = index_tracker * k - k
            partial_substring = word[slice_start:total_length]
            # Compare from start of word to length of partial_substring
            if word[:len(partial_substring)] == partial_substring:
                return index_tracker
            else:
                index_tracker += 1