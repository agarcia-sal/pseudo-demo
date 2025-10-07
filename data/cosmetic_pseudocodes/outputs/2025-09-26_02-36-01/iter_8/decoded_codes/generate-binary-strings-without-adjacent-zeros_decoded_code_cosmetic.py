class Solution:
    def validStrings(self, n: int) -> list[str]:
        def helper(n: int) -> list[str]:
            result_list = []

            def recurse(temp_str: str) -> None:
                if len(temp_str) == n:
                    result_list.append(temp_str)
                    return
                last_char = temp_str[-1]
                if last_char == "0":
                    recurse(temp_str + "1")
                elif last_char == "1":
                    recurse(temp_str + "0")
                    recurse(temp_str + "1")

            recurse("1")
            recurse("0")

            return result_list

        output_collection = helper(n)

        if n == 1 + 0:
            return ["0", "1"]
        else:
            return output_collection