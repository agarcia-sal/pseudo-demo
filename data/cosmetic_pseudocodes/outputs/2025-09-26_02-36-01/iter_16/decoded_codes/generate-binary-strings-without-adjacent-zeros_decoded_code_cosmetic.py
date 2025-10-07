from typing import List

class Solution:
    def validStrings(self, size: int) -> List[str]:
        # Base case: if size == 1, return ["0", "1"]
        if size == 1:
            return ["0", "1"]

        validTrees = []

        def backtrack_sequence(input_seq: str) -> None:
            if len(input_seq) == size:
                validTrees.append(input_seq)
                return

            last_idx = len(input_seq) - 1
            if input_seq[last_idx] == "1":
                backtrack_sequence(input_seq + "0")
                backtrack_sequence(input_seq + "1")
            else:  # input_seq[last_idx] == "0"
                backtrack_sequence(input_seq + "1")

        backtrack_sequence("0")
        backtrack_sequence("1")

        return validTrees