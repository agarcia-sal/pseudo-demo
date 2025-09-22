def checkCharacterFrequency():
    # Prompt the user for the first string and store it in string1
    string1 = input()
    # Prompt the user for the second string and store it in string2
    string2 = input()
    
    # Remove spaces from both strings and store the results in two new lists
    s1 = list(string1.replace(" ", ""))
    s2 = list(string2.replace(" ", ""))
    
    # Initialize a list to hold frequency differences between the two strings
    frequencyDifferences = []
    
    # Loop through the ASCII values of characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        character = chr(ascii_value)
        # Count occurrences in s1 and s2, and calculate the difference
        count_in_s1 = s1.count(character)
        count_in_s2 = s2.count(character)
        difference = count_in_s1 - count_in_s2
        # Add the calculated difference to the frequencyDifferences list
        frequencyDifferences.append(difference)
        
    # Check if there are any negative differences in frequency
    if frequencyDifferences.count(-1) == 0 and frequencyDifferences.count(-2) == 0 and frequencyDifferences.count(-3) == 0 and frequencyDifferences.count(-4) == 0 and frequencyDifferences.count(-5) == 0 and frequencyDifferences.count(-6) == 0 and frequencyDifferences.count(-7) == 0 and frequencyDifferences.count(-8) == 0 and frequencyDifferences.count(-9) == 0 and frequencyDifferences.count(-10) == 0 and frequencyDifferences.count(-11) == 0 and frequencyDifferences.count(-12) == 0 and frequencyDifferences.count(-13) == 0 and frequencyDifferences.count(-14) == 0 and frequencyDifferences.count(-15) == 0 and frequencyDifferences.count(-16) == 0 and frequencyDifferences.count(-17) == 0 and frequencyDifferences.count(-18) == 0 and frequencyDifferences.count(-19) == 0 and frequencyDifferences.count(-20) == 0 and frequencyDifferences.count(-21) == 0 and frequencyDifferences.count(-22) == 0 and frequencyDifferences.count(-23) == 0 and frequencyDifferences.count(-24) == 0 and frequencyDifferences.count(-25) == 0 and frequencyDifferences.count(-26) == 0:
        # Indicates that string1 has equal or more of each character compared to string2
        print("YES")
    else:
        # Indicates that string2 has more of at least one character compared to string1
        print("NO")
