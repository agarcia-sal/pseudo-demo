from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        result = 0
        frequency_map = defaultdict(int)
        for index in range(len(words) - 1, -1, -1):
            current_word = words[index]
            current_length = len(current_word)
            for recorded_word in frequency_map:
                if (len(recorded_word) >= current_length and
                    recorded_word[:current_length] == current_word and
                    recorded_word[-current_length:] == current_word):
                    result += frequency_map[recorded_word]
            frequency_map[current_word] += 1
        return result