# Function to check if the first string can form the characters in the second string
def can_form_string():
    # Receive Input
    first_string = input()  # Store user input for the first string
    second_string = input()  # Store user input for the second string

    # Process Input: Remove all spaces
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")

    # Initialize Frequency Count: Create a list for character frequencies
    character_frequencies = [0] * 256  # Assuming ASCII characters

    # Count Character Frequencies
    for char in cleaned_first_string:
        character_frequencies[ord(char)] += 1  # Increment count for the character in the first string
    for char in cleaned_second_string:
        character_frequencies[ord(char)] -= 1  # Decrement count for the character in the second string

    # Evaluate Frequencies
    has_shortages = 'NO'  # Initialize shortage flag to 'NO'
    for count in character_frequencies:
        if count < 0:  # If any count is negative, there are shortages
            has_shortages = 'YES'
            break

    # Output Result
    if has_shortages == 'NO':
        print("YES")  # First string can form the second string
    else:
        print("NO")  # Shortage of characters

# Call the function to run the check
can_form_string()
