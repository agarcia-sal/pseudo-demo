def calculateRemainingPackages(numberOfItems, packageSize):
    quotient, remainder = divmod(numberOfItems, packageSize)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return numberOfItems

# Main Program
n = int(input())
m = int(input())
s = int(input())

# Calculate the remaining packages for both sets of items
remainingPackagesForN = calculateRemainingPackages(n, s)
remainingPackagesForM = calculateRemainingPackages(m, s)

# Output the product of the two results
print(remainingPackagesForN * remainingPackagesForM)
