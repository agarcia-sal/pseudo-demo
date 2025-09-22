def calculateAdjustedGroups(number, groupSize):
    # Divide the number into full groups of the specified size
    ful = number // groupSize
    rem = number % groupSize
    
    # If there is a remainder, meaning there are extra items
    if rem > 0:
        # Return the total groups including the extra items
        return rem * (ful + 1)
    else:
        # If everything fits perfectly into groups, return the original number
        return number

# Read the inputs from the user (expected to be three integers)
inp = list(map(int, input().split()))
n = inp[0]  # First value
m = inp[1]  # Second value
s = inp[2]  # Group size

# Calculate the adjusted group counts for n and m
adjN = calculateAdjustedGroups(n, s)
adjM = calculateAdjustedGroups(m, s)

# Calculate and display the product of the adjusted group counts
print(adjN * adjM)
