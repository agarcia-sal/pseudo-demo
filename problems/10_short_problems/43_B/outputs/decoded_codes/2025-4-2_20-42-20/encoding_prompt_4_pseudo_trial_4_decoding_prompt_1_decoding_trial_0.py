def check_character_frequency_difference():
    s1 = []
    s2 = []
    
    # For each of the two user inputs
    for i in range(2):
        # Read the input string
        input_string = input()
        
        # Remove all spaces from the string
        cleaned_string = input_string.replace(" ", "")
        
        # Store the cleaned string in the corresponding list (s1 or s2)
        if i == 0:
            s1.append(cleaned_string)
        else:
            s2.append(cleaned_string)
    
    # Initialize a frequency difference list, freqs
    freqs = []
    
    # For each character code from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        # Calculate the difference in occurrence of the character in s1 and s2
        count_s1 = sum(s.count(char) for s in s1)
        count_s2 = sum(s.count(char) for s in s2)
        difference = count_s1 - count_s2
        
        # Store this difference in the freqs list
        freqs.append(difference)
    
    # If there are no negative values in the freqs list
    if all(freq >= 0 for freq in freqs):
        # Output "YES"
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Call the function
check_character_frequency_difference()
