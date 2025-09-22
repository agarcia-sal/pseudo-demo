def main():
    # Step 1: Input two strings from the user
    string_one = input()
    string_two = input()
    
    # Step 2: Process the Strings to filter out spaces
    filtered_string_one = [char for char in string_one if char != ' ']
    filtered_string_two = [char for char in string_two if char != ' ']

    # Step 3: Count Character Frequencies
    # Initialize a list for frequency differences (characters from ASCII value A to z)
    frequency_difference = [0] * 123  # ASCII values from 0 to 122
    
    # Count characters in filtered_string_one
    for char in filtered_string_one:
        frequency_difference[ord(char)] += 1
    
    # Count characters in filtered_string_two
    for char in filtered_string_two:
        frequency_difference[ord(char)] -= 1

    # Step 4: Check Frequency Conditions
    negative_counts = [count for count in frequency_difference if count < 0]

    # Step 5: Output based on conditions
    if not negative_counts:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
