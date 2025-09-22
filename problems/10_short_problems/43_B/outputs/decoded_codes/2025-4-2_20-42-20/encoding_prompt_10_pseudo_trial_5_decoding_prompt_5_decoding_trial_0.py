# Function to compare two strings and determine if they have the same character frequencies
def compare_string_frequencies():
    # Receive Input
    string1 = input()
    string2 = input()
    
    # Initialize Variables
    cleaned_string1 = string1.replace(" ", "")
    cleaned_string2 = string2.replace(" ", "")
    
    # Initialize Frequency List
    frequency_differences = []
    
    # Calculate Character Frequencies
    for ascii_code in range(65, 123):  # From 'A' (65) to 'z' (122)
        # Calculate frequency difference for current character
        char_freq_diff = cleaned_string1.count(chr(ascii_code)) - cleaned_string2.count(chr(ascii_code))
        frequency_differences.append(char_freq_diff)
    
    # Check for Negative Frequencies
    negative_count = sum(1 for freq in frequency_differences if freq < 0)
    
    # Output Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Function call to execute the comparisons
compare_string_frequencies()
