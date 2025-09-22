def check_character_distribution():
    
    # Step 1: Read two strings from user input
    firstString = input().replace(" ", "")
    secondString = input().replace(" ", "")
    
    # Step 2: Initialize an array to hold frequency differences
    # Considering the ASCII character range from 'A' to 'z', we create a list of size 128
    frequency_differences = [0] * 128

    # Step 3: Calculate the frequency difference for each character
    for char in range(65, 123):  # ASCII values for 'A' to 'Z' and 'a' to 'z'
        count_first = firstString.count(chr(char))
        count_second = secondString.count(chr(char))
        frequency_differences[char] = count_first - count_second
    
    # Step 4: Check if any character has a negative frequency difference
    negative_count = 0
    for difference in frequency_differences:
        if difference < 0:
            negative_count += 1
            
    # Step 5: Determine if the character distributions are valid
    if negative_count == 0:
        print("YES")  # implying firstString can cover secondString
    else:
        print("NO")   # implying firstString cannot cover secondString

# Example of function execution
check_character_distribution()


from collections import Counter

def check_character_distribution():
    
    # Step 1: Read two strings from user input
    firstString = input().replace(" ", "")
    secondString = input().replace(" ", "")

    # Step 2: Count characters in both strings using Counter
    count_first = Counter(firstString)
    count_second = Counter(secondString)

    # Step 3: Check the character frequencies
    for char in count_second:
        if count_first[char] < count_second[char]:
            print("NO")  # implying firstString cannot cover secondString
            return

    # Step 4: If all checks pass
    print("YES")  # implying firstString can cover secondString

# Example of function execution
check_character_distribution()
