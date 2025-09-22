def get_input():
    # Read input from the user, removing any spaces
    return input().replace(" ", "")

def count_character_frequencies(s):
    # Create an empty dictionary to count character frequencies
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def can_transform(firstInput, secondInput):
    # Count character frequencies for both strings
    freq_first = count_character_frequencies(firstInput)
    freq_second = count_character_frequencies(secondInput)

    # Evaluate character frequency differences
    for char in freq_second:
        if freq_second[char] > freq_first.get(char, 0):
            return "NO"
    return "YES"

def main():
    # Get the first and second input strings
    firstInput = get_input()
    secondInput = get_input()
    
    # Check if firstInput can match secondInput
    result = can_transform(firstInput, secondInput)
    
    # Output the result
    print(result)

# Execute the main function
if __name__ == "__main__":
    main()
