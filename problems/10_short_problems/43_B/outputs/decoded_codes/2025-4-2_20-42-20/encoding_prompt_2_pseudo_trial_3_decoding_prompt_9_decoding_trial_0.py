# Accept two strings from the user
stringOne = input()
stringTwo = input()

# Process the strings to remove spaces
filteredStringOne = [char for char in stringOne if char != ' ']
filteredStringTwo = [char for char in stringTwo if char != ' ']

# Initialize a list to keep track of frequency differences
frequencyDifference = []

# Count character frequencies from ASCII values 'A' (65) to 'z' (122)
for ascii_value in range(65, 123):
    countOne = filteredStringOne.count(chr(ascii_value))
    countTwo = filteredStringTwo.count(chr(ascii_value))
    
    # Calculate the difference and store it in frequencyDifference
    frequencyDifference.append(countOne - countTwo)

# Create a list of negative counts
negativeCounts = [count for count in frequencyDifference if count < 0]

# Check if any negative counts exist
if not negativeCounts:  # If negativeCounts is empty
    print("YES")
else:
    print("NO")
