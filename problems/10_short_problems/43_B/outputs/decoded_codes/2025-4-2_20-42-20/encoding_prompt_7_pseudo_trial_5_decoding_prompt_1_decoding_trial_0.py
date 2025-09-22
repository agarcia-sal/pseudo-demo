def checkCharacterFrequency():
    firstString = input()
    secondString = input()

    firstFilteredList = [char for char in firstString if char != ' ']
    secondFilteredList = [char for char in secondString if char != ' ']

    frequencyDifferenceList = []

    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)

        frequency_in_first = firstFilteredList.count(current_char)
        frequency_in_second = secondFilteredList.count(current_char)
        
        frequencyDifference = frequency_in_first - frequency_in_second
        frequencyDifferenceList.append(frequencyDifference)

    if all(diff >= 0 for diff in frequencyDifferenceList):
        print("YES")
    else:
        print("NO")

# To invoke the function
checkCharacterFrequency()
