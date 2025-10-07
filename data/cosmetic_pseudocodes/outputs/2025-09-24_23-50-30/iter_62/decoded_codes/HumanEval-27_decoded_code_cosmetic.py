def flip_case(parameter_one: str) -> str:
    def helper(index: int, accumulator: str) -> str:
        if index == len(parameter_one):
            return accumulator
        current_char = parameter_one[index]
        toggled_char = current_char.upper() if current_char.islower() else current_char.lower()
        return helper(index + 1, accumulator + toggled_char)
    return helper(0, "")