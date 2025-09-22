def get_input(prompt):
    """Get user input, ensuring no prompt text is included as per the guidelines."""
    return input()

def count_character_frequency(string):
    """Count the frequency of each character in the string."""
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def can_form_string(first_input, second_input):
    """Determine if first_input can be rearranged to form second_input."""
    char_count_first = count_character_frequency(first_input)
    char_count_second = count_character_frequency(second_input)
    
    # Check if first_input has equal or more characters than second_input for all characters
    for char in char_count_second:
        if char_count_first.get(char, 0) < char_count_second[char]:
            return "NO"
    
    return "YES"

def main():
    """Main function to handle user inputs and output the result."""
    first_input = get_input().replace(" ", "")
    second_input = get_input().replace(" ", "")
    
    result = can_form_string(first_input, second_input)
    print(result)

# Entry point of the program
if __name__ == "__main__":
    main()


    aabbcc
    abc
    

    aabb
    aabbc
    

    abcdef
    abcdef
    