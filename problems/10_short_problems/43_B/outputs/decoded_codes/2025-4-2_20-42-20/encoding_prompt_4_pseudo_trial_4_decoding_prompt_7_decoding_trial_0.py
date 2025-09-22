def check_frequency_difference():
    # Step 2: Initialize two empty lists for the two input strings
    s1 = []
    s2 = []
    
    # Step 3: Read two user inputs
    for i in range(2):
        # Step 3a: Read the input string
        user_input = input()
        # Step 3b: Remove all spaces from the string
        cleaned_input = user_input.replace(" ", "")
        # Step 3c: Store the cleaned string in the corresponding list (s1 or s2)
        if i == 0:
            s1.append(cleaned_input)
        else:
            s2.append(cleaned_input)
    
    # Join the cleaned strings as we need the full string for frequency analysis
    s1 = ''.join(s1)
    s2 = ''.join(s2)
    
    # Step 4: Initialize a frequency difference list
    freqs = []
    
    # Step 5: Calculate frequency differences for characters A-Z and a-z
    for char in range(ord('A'), ord('z') + 1):
        # Get the character corresponding to the ASCII code
        char = chr(char)
        # Step 5a: Calculate the occurrence of the character in s1 and s2
        count_s1 = s1.count(char)
        count_s2 = s2.count(char)
        # Step 5b: Store the difference in the freqs list
        freqs.append(count_s1 - count_s2)
    
    # Step 6: Evaluate frequency differences
    if all(freq >= 0 for freq in freqs):
        # Step 6a: Output "YES" if no negative values in freqs
        print("YES")
    else:
        # Step 7a: Otherwise, output "NO"
        print("NO")

# Wrap the function call within a typical main guard
if __name__ == "__main__":
    check_frequency_difference()
