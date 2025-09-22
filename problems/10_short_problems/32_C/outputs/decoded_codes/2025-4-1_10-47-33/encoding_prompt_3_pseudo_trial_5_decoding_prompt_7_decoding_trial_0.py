def calculateRemainingPackages(numberOfItems, packageSize):
    # Calculate quotient and remainder when dividing numberOfItems by packageSize
    quotient = numberOfItems // packageSize
    remainder = numberOfItems % packageSize

    # If there is a remainder, the remaining packages are remainder * (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return the total number of items
        return numberOfItems

# Begin the main program
# Read inputs for number of items (n), another value (m), and package size (s)
numberOfItems = int(input())
anotherValue = int(input())
packageSize = int(input())

# Calculate the remaining packages for both sets of items
remainingPackagesForN = calculateRemainingPackages(numberOfItems, packageSize)
remainingPackagesForM = calculateRemainingPackages(anotherValue, packageSize)

# Output the product of the two results
print(remainingPackagesForN * remainingPackagesForM)
