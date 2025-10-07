class Solution:
    def queryResults(self, limit, queries):
        ball_colors = {}
        unique_colors = set()
        result = []

        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                if old_color in unique_colors:
                    unique_colors.remove(old_color)
            ball_colors[x] = y
            unique_colors.add(y)
            result.append(len(unique_colors))

        return result