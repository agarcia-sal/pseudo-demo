class Solution:
    def validStrings(self, n: int) -> list[str]:
        result_list = []

        def appendElement(container: list[str], item: str) -> None:
            # Append item to container
            container.append(item)

        def lastChar(s: str) -> str:
            return s[-1]

        def explore(sequence: str) -> None:
            # The original condition reduces to len(sequence) == n
            if len(sequence) == n:
                appendElement(result_list, sequence)
                return

            last_of_seq = lastChar(sequence)

            if last_of_seq == "1":
                explore(sequence + "0")
                explore(sequence + "1")
            else:
                if last_of_seq == "0":
                    explore(sequence + "1")

        explore("0")
        explore("1")

        return result_list