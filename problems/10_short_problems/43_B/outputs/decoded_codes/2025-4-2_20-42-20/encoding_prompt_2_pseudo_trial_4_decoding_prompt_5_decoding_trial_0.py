# Function to compare character frequencies in two strings
def compare_string_frequencies():
    # Receive input strings from the user
    input_string1 = input()
    input_string2 = input()
    
    # Remove spaces from both input strings
    cleaned_string1 = input_string1.replace(" ", "")
    cleaned_string2 = input_string2.replace(" ", "")
    
    # Initialize a list to store frequency differences
    frequency_differences = []
    
    # Calculate frequency differences for characters from ASCII 'A' to 'z'
    for ascii_value in range(65, 123):  # ASCII values from 'A'(65) to 'z'(122)
        # Get the character for the current ASCII value
        character = chr(ascii_value)
        
        # Count occurrences of the character in both cleaned strings
        count_in_string1 = cleaned_string1.count(character)
        count_in_string2 = cleaned_string2.count(character)
        
        # Calculate the difference in counts
        difference = count_in_string1 - count_in_string2
        
        # Store the difference in the frequency_differences list
        frequency_differences.append(difference)
    
    # Create a list of negative differences
    negative_differences = [diff for diff in frequency_differences if diff < 0]
    
    # Check if there are no negative differences
    if not negative_differences:  # If the list is empty
        print("YES")  # All counts in string1 are greater than or equal to those in string2
    else:
        print("NO")   # There are characters in string2 with higher counts than in string1

# Calling the function to execute the frequency comparison
compare_string_frequencies()
