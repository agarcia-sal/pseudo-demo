def check_character_frequency_difference():
    # Initialize two empty lists to store cleaned input strings
    cleaned_strings = ["", ""]
    
    # Read two user inputs and clean the strings by removing spaces
    for i in range(2):
        user_input = input()
        cleaned_strings[i] = user_input.replace(" ", "")
        
    # Initialize a frequency difference list with zero for each character from 'A' to 'z'
    frequency_difference = [0] * (ord('z') + 1)
    
    # Calculate frequency differences for each character in both strings
    for char in cleaned_strings[0]:  # first string's characters
        frequency_difference[ord(char)] += 1
    
    for char in cleaned_strings[1]:  # second string's characters
        frequency_difference[ord(char)] -= 1

    # Check for negative values in the frequency difference list
    if all(diff >= 0 for diff in frequency_difference):
        print("YES")  # Outputs "YES" if all values are non-negative
    else:
        print("NO")   # Outputs "NO" if any value is negative

# Call the function to execute the character frequency check
check_character_frequency_difference()
