def compare_character_frequencies():
    # Get the first string input from the user and remove spaces
    first_string = input().replace(" ", "")
    
    # Get the second string input from the user and remove spaces
    second_string = input().replace(" ", "")
    
    # Initialize a list to hold frequency differences for each character from 'A' to 'z'
    frequency_differences = []
    
    # Loop through ASCII values from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):
        # Count occurrences in the first cleaned string
        first_count = first_string.count(chr(char_code))
        # Count occurrences in the second cleaned string
        second_count = second_string.count(chr(char_code))
        # Calculate the difference and store it
        frequency_differences.append(first_count - second_count)
    
    # Check if all values in frequency differences are greater than or equal to zero
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")  # Frequencies match
    else:
        print("NO")   # Frequencies do not match

# Example usage:
# If you want to test the function, call it after defining it:
# compare_character_frequencies()
