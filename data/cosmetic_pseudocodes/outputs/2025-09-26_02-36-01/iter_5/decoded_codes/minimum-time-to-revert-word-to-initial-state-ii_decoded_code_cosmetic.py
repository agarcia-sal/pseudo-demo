class Solution:
    def minimumTimeToInitialState(self, input_word: str, key: int) -> int:
        total_length = len(input_word)

        def checkPrefix(index: int) -> int:
            if index > total_length:
                return -1
            segment = input_word[index * key:]
            if input_word.startswith(segment):
                return index
            else:
                return checkPrefix(index + 1)

        return checkPrefix(1)