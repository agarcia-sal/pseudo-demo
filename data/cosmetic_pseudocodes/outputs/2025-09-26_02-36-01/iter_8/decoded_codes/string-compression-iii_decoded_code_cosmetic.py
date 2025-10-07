class Solution:
    def compressedString(self, word: str) -> str:
        accumulation = []
        index_tracker = 0
        while index_tracker < len(word):
            current_char = word[index_tracker]
            occurrence = 0
            while index_tracker < len(word) and word[index_tracker] == current_char:
                occurrence += 1
                index_tracker += 1
                if occurrence == 9:
                    break
            segment = str(occurrence) + current_char
            accumulation.append(segment)
        output = ""
        iter_count = 0
        while iter_count < len(accumulation):
            output += accumulation[iter_count]
            iter_count += 1
        return output