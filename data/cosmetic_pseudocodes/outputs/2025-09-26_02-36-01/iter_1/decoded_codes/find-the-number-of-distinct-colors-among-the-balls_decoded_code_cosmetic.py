class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_colors = {}
        unique_colors = set()
        result = []

        for query in queries:
            x = query[0]
            y = query[1]

            if x in ball_colors:
                old_color = ball_colors[x]
                if old_color in unique_colors:
                    unique_colors.remove(old_color)

            ball_colors[x] = y
            unique_colors.add(y)
            result.append(len(unique_colors))

        return result