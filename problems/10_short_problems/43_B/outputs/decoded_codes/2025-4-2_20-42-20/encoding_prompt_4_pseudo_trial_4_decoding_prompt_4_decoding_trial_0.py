def check_character_frequency_difference():
    # Step 2: Initialize two empty lists for the cleaned strings
    s1 = []
    s2 = []
    
    # Step 3: Get user inputs and process the strings
    for i in range(2):
        # Read input and remove spaces
        user_input = input()
        cleaned_input = user_input.replace(" ", "")
        
        # Store the cleaned strings in the corresponding list
        if i == 0:
            s1.append(cleaned_input)
        else:
            s2.append(cleaned_input)
    
    # Concatenate both lists to get the final strings
    str1 = ''.join(s1)
    str2 = ''.join(s2)
    
    # Step 4: Initialize a frequency difference list
    freqs = [0] * (ord('z') - ord('A') + 1)  # Covers A-Z and a-z

    # Step 5: Calculate frequency differences for each character
    for char_code in range(ord('A'), ord('z') + 1):
        # Count characters in each string
        count1 = str1.count(chr(char_code))
        count2 = str2.count(chr(char_code))
        
        # Store the difference in freqs list
        freqs[char_code - ord('A')] = count1 - count2

    # Step 6: Check for negative values in the frequency difference list
    if all(freq >= 0 for freq in freqs):
        # Step 7a: Output "YES"
        print("YES")
    else:
        # Step 7b: Output "NO"
        print("NO")

# Call the function to execute
check_character_frequency_difference()
