def compare_strings():
    # Receive Input
    s1 = input()
    s2 = input()
    
    # Initialize Variables
    cleaned_s1 = s1.replace(" ", "")  # Remove spaces from s1
    cleaned_s2 = s2.replace(" ", "")  # Remove spaces from s2
    
    # Initialize Frequency List
    freqs = []
    
    # Calculate Character Frequencies
    for x in range(65, 123):  # ASCII values from 'A' to 'z'
        freq_difference = cleaned_s1.count(chr(x)) - cleaned_s2.count(chr(x))
        freqs.append(freq_difference)
    
    # Check for Negative Frequencies
    negative_count = sum(1 for freq in freqs if freq < 0)
    
    # Output Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to run the comparison
compare_strings()
