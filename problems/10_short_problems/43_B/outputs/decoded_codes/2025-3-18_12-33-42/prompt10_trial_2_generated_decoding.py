def process_input_string():
    """Read an input string, remove spaces, and return it as a list of characters."""
    raw_string = input()
    return list(raw_string.replace(" ", ""))

def character_frequency_difference(s1, s2):
    """Calculate the frequency difference between two strings for characters in the ASCII range."""
    # Initialize frequency differences for ASCII characters from 'A' (65) to 'z' (122)
    freqs = [0] * (123)  # Index 0-122 represent 'A' to 'z'
    
    # Count occurrences of each character in s1
    for char in s1:
        freqs[ord(char)] += 1
        
    # Count occurrences of each character in s2
    for char in s2:
        freqs[ord(char)] -= 1
    
    return freqs

def main():
    """Main function to execute the program logic."""
    # Read and process input strings
    s1 = process_input_string()
    s2 = process_input_string()
    
    # Get frequency differences
    freqs = character_frequency_difference(s1, s2)
    
    # Count negative frequencies
    negative_count = sum(1 for freq in freqs if freq < 0)
    
    # Output the result based on negative frequencies count
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Execute the program
if __name__ == "__main__":
    main()
