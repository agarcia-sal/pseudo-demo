def main():
    # Step 1: Get user input
    string1 = input()
    string2 = input()

    # Step 2: Clean the input strings by removing spaces
    clean_string1 = string1.replace(" ", "")
    clean_string2 = string2.replace(" ", "")

    # Step 3: Initialize a dictionary to hold frequency differences
    # Using ASCII values from 'A' (65) to 'z' (122)
    frequency_differences = {chr(i): 0 for i in range(65, 123)}

    # Step 4: Calculate the frequency of each character
    for char in range(65, 123):  # From 'A' to 'z'
        char = chr(char)
        count_in_string1 = clean_string1.count(char)
        count_in_string2 = clean_string2.count(char)
        frequency_differences[char] = count_in_string1 - count_in_string2

    # Step 5: Check if all frequency differences are non-negative
    if all(difference >= 0 for difference in frequency_differences.values()):
        print("YES")
    else:
        print("NO")

# Running the main function
if __name__ == "__main__":
    main()
