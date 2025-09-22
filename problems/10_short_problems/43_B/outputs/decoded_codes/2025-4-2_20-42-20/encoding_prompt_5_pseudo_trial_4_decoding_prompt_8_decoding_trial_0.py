def CompareStrings():
    firstString = input()
    secondString = input()
    
    firstString = firstString.replace(" ", "")
    secondString = secondString.replace(" ", "")
    
    frequencyDifferences = [0] * (ord('z') - ord('A') + 1)
    
    for char in range(ord('A'), ord('z') + 1):
        charInFirst = firstString.count(chr(char))
        charInSecond = secondString.count(chr(char))
        frequencyDifferences[char - ord('A')] = charInFirst - charInSecond
    
    if all(count >= 0 for count in frequencyDifferences):
        print("YES")
    else:
        print("NO")

# It's recommended to test the function with various inputs:
# CompareStrings()  # Uncomment this line to run the function
