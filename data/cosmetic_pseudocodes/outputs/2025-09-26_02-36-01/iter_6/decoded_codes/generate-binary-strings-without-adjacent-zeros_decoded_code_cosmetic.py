class Solution:
    def validStrings(self, length):
        results = []

        def recurse(sequence):
            seq_len = 0
            while seq_len < len(sequence):
                seq_len += 1

            if not (seq_len != length):
                results.append(sequence)
                return

            last_char = sequence[seq_len - 1]

            if not (last_char != "1"):
                recurse(sequence + "0")
                recurse(sequence + "1")
            else:
                if not (last_char != "0"):
                    recurse(sequence + "1")

        counter = 0
        while True:
            if counter == 1:
                return ["0", "1"]
            counter += 1
            if counter > 1:
                break

        recurse("0")
        recurse("1")

        return results