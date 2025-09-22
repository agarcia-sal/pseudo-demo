# Function to determine if the first string can be transformed into the second string
def can_transform_strings():
    # Gather input strings
    first_input = input()
    second_input = input()
    
    # Process strings to remove spaces
    first_string = [char for char in first_input if char != ' ']
    second_string = [char for char in second_input if char != ' ']
    
    # Initialize a list for frequency differences (size 256 for ASCII values)
    frequency_differences = [0] * 256
    
    # Calculate frequency for each character from 'A' to 'z'
    for char_code in range(65, 123):  # from 'A' (65) to 'z' (122)
        char = chr(char_code)
        first_count = first_string.count(char)
        second_count = second_string.count(char)
        
        # Store the difference in frequency
        frequency_differences[char_code] = first_count - second_count
    
    # Determine if transformation is possible
    if all(count >= 0 for count in frequency_differences):
        print("YES")
    else:
        print("NO")

# Run the function
can_transform_strings()
