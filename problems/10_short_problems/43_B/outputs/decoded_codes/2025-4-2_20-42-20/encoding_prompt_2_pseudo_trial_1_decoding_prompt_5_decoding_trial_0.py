# Function to evaluate character frequency differences between two strings
def evaluate_character_frequencies():
    # Input Reading
    first_string = input()
    second_string = input()

    # String Preprocessing
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")
    
    # Frequency Calculation
    character_frequencies = []
    for char in range(ord('A'), ord('z') + 1):
        char = chr(char)  # Convert ASCII value back to character
        first_count = cleaned_first_string.count(char)
        second_count = cleaned_second_string.count(char)
        difference = first_count - second_count
        character_frequencies.append(difference)

    # Result Evaluation
    negative_count = sum(1 for freq in character_frequencies if freq < 0)
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function
evaluate_character_frequencies()
