def checkCharacterFrequency():
    firstString = input()
    secondString = input()
    
    firstFilteredList = [char for char in firstString if char != ' ']
    secondFilteredList = [char for char in secondString if char != ' ']

    frequencyDifferenceList = []

    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)
        frequency_difference = firstFilteredList.count(current_char) - secondFilteredList.count(current_char)
        frequencyDifferenceList.append(frequency_difference)

    if all(diff >= 0 for diff in frequencyDifferenceList):
        print("YES")
    else:
        print("NO")

# Run the function to test it
checkCharacterFrequency()
