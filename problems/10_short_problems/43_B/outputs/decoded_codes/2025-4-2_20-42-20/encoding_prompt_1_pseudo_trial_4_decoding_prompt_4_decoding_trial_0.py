def main():
    # Input two strings from user, removing any spaces
    s1 = input().replace(" ", "")
    s2 = input().replace(" ", "")
    
    # Initialize a list to hold frequency differences for ASCII characters from 'A' to 'z'
    frequency_diff = [0] * (ord('z') - ord('A') + 1)

    # Calculate frequency difference for every character in the ASCII range
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        count_in_s1 = s1.count(char)
        count_in_s2 = s2.count(char)
        frequency_diff[char_code - ord('A')] = count_in_s1 - count_in_s2

    # Count how many differences are negative
    negative_count = sum(1 for diff in frequency_diff if diff < 0)

    # Output "YES" if there are no negative differences, otherwise "NO"
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the code
if __name__ == "__main__":
    main()
