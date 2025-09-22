def can_construct_string(first_string, second_string):
    # Remove spaces from both input strings
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    
    # Initialize a list to track character counts for ASCII characters
    character_differences = [0] * 128  # Covers ASCII characters
    
    # Count frequency of each character in the first string
    for char in first_string:
        character_differences[ord(char)] += 1
        
    # Count frequency of each character in the second string
    for char in second_string:
        character_differences[ord(char)] -= 1
    
    # Check for negative values in character_differences
    for difference in character_differences:
        if difference < 0:
            return "NO"
    
    return "YES"

# Input from the user
first_string = input()
second_string = input()

# Call the function and print the result
result = can_construct_string(first_string, second_string)
print(result)
