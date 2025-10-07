from typing import List

def f(input_var: int) -> List[int]:
    output_seq: List[int] = []
    index: int = 1
    while index <= input_var:
        if index % 2 == 0:
            temp_factor: int = 1
            counter: int = 1
            while counter <= index:
                temp_factor *= counter
                counter += 1
            output_seq.append(temp_factor)
        else:
            temp_sum: int = 0
            counter: int = 1
            while counter <= index:
                temp_sum += counter
                counter += 1
            output_seq.append(temp_sum)
        index += 1
    return output_seq