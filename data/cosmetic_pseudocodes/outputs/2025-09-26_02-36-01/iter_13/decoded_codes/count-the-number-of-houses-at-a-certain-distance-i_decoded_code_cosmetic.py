from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        output = [0] * n

        def breadth_first_search(origin: int) -> None:
            discovered = [False] * (n + 1)
            levels = [0] * (n + 1)
            line = [origin]
            discovered[origin] = True

            while line:
                active = line.pop(0)

                def process_neighbor(destination: int) -> None:
                    if 1 <= destination <= n and not discovered[destination]:
                        discovered[destination] = True
                        levels[destination] = levels[active] + 1
                        line.append(destination)

                process_neighbor(active - 1)
                process_neighbor(active + 1)

                if active == x and not discovered[y]:
                    discovered[y] = True
                    levels[y] = levels[active] + 1
                    line.append(y)

                if active == y and not discovered[x]:
                    discovered[x] = True
                    levels[x] = levels[active] + 1
                    line.append(x)

            def increment_result_by_distance(index: int) -> None:
                if levels[index] > 0:
                    idx = levels[index] - 1
                    output[idx] += 1

            for i in range(1, n + 1):
                increment_result_by_distance(i)

        def loop_bfs(counter: int) -> None:
            if counter > n:
                return
            breadth_first_search(counter)
            loop_bfs(counter + 1)

        loop_bfs(1)
        return output