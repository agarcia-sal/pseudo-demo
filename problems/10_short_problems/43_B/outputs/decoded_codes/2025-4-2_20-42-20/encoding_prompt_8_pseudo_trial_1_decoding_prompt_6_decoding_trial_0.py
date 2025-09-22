# Define the main function
def main():
    # Get user input
    first_string = input()  # Input for the first string
    second_string = input()  # Input for the second string

    # Prepare strings by removing spaces
    cleaned_first_string = ''.join(first_string.split())  # Remove spaces from first string
    cleaned_second_string = ''.join(second_string.split())  # Remove spaces from second string

    # Initialize frequency list for characters a-z and A-Z
    character_frequency = [0] * 52  # 26 for lowercase, 26 for uppercase

    # Function to update character frequency
    def update_frequency(string, increment):
        for char in string:
            if 'A' <= char <= 'Z':  # Uppercase
                index = ord(char) - ord('A')  # Map A-Z to 0-25
                character_frequency[index] += increment
            elif 'a' <= char <= 'z':  # Lowercase
                index = ord(char) - ord('a') + 26  # Map a-z to 26-51
                character_frequency[index] += increment

    # Count characters from cleaned first string
    update_frequency(cleaned_first_string, 1)  # Increment frequency for first string

    # Count characters from cleaned second string
    update_frequency(cleaned_second_string, -1)  # Decrement frequency for second string

    # Check character sufficiency
    is_sufficient = True  # Assume it is sufficient initially
    for count in character_frequency:
        if count < 0:  # If any count is negative, it's insufficient
            is_sufficient = False
            break

    # Output the result
    if is_sufficient:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
