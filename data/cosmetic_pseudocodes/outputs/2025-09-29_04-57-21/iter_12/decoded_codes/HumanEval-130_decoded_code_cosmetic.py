from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n != 0:
        result_list: List[int] = [1, 3]
        counter: int = 2
        while counter <= integer_n:
            if (counter % 2) != 0:
                val1 = result_list[counter - 1] + result_list[counter - 2] + ((counter + 3) // 2)
                result_list.append(val1)
            else:
                val2 = (counter // 2) + 1
                result_list.append(val2)
            counter += 1
        return result_list
    else:
        return [1]