def check_character_frequency_difference():
    # Step 2: Initialize two empty lists
    s1 = []
    s2 = []
    
    # Step 3: For each of the two user inputs
    for i in range(2):
        # Step 3a: Read the input string
        input_string = input()
        # Step 3b: Remove all spaces from the string
        cleaned_string = input_string.replace(" ", "")
        # Step 3c: Store the cleaned string in the corresponding list (s1 or s2)
        if i == 0:
            s1 = cleaned_string
        else:
            s2 = cleaned_string
    
    # Step 4: Initialize a frequency difference list
    freqs = []

    # Step 5: For each character code from 'A' to 'z'
    for code in range(ord('A'), ord('z') + 1):
        # Step 5a: Calculate the difference in occurrence of the character in s1 and s2
        char = chr(code)
        diff = s1.count(char) - s2.count(char)
        # Step 5b: Store this difference in the freqs list
        freqs.append(diff)

    # Step 6: If there are no negative values in the freqs list
    if all(f >= 0 for f in freqs):
        # Step 6a: Output "YES"
        print("YES")
    else:
        # Step 7a: Output "NO"
        print("NO")

# Call the function to execute
check_character_frequency_difference()
