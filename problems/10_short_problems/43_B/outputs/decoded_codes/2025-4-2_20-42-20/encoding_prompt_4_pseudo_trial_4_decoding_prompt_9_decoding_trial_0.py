def check_character_frequency_difference():
    # Initialize two empty lists to store cleaned strings
    s1 = []
    s2 = []
    
    # Read the first input string and clean it
    input1 = input()
    cleaned_input1 = input1.replace(" ", "")
    s1.append(cleaned_input1)
    
    # Read the second input string and clean it
    input2 = input()
    cleaned_input2 = input2.replace(" ", "")
    s2.append(cleaned_input2)
    
    # Initialize a frequency difference list
    freqs = []
    
    # Loop through character codes from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):
        # Calculate the occurrence of the character in both strings
        count_s1 = s1[0].count(chr(char_code))
        count_s2 = s2[0].count(chr(char_code))
        
        # Calculate the difference in occurrence
        diff = count_s1 - count_s2
        
        # Store the difference in the freqs list
        freqs.append(diff)
    
    # Check if there are any negative values in the freqs list
    if all(freq >= 0 for freq in freqs):
        print("YES")
    else:
        print("NO")
