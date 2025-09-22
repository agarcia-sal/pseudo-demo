def compare_strings():
    # Read user input for the first string and remove spaces
    first_string = input().replace(" ", "")
    # Read user input for the second string and remove spaces
    second_string = input().replace(" ", "")
    
    # Initialize a frequency differences list to count character frequencies from 'A' to 'z'
    frequency_differences = [0] * 128  # To accommodate ASCII characters

    # Count character frequencies from the first string
    for char in first_string:
        frequency_differences[ord(char)] += 1

    # Subtract character frequencies based on the second string
    for char in second_string:
        frequency_differences[ord(char)] -= 1

    # Check if any frequency difference is negative
    for frequency in frequency_differences:
        if frequency < 0:
            print("NO")
            return
            
    # If no negative frequencies are found, print "YES"
    print("YES")

# Example usage: Call the function to run the comparison
compare_strings()
