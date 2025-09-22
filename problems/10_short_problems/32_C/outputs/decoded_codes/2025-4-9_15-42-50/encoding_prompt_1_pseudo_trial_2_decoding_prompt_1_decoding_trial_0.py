def CalculateMaxItems(num1, size):
    ful = num1 // size  # Integer division to get the number of full groups
    lef = num1 % size   # Get the remainder

    if lef > 0:
        return lef * (ful + 1)  # Calculate new maximum items including leftover
    else:
        return num1  # If no leftover, return the original number

# Main Program:
tot1 = int(input())  # Read the total items from the first set
tot2 = int(input())  # Read the total items from the second set
gro = int(input())   # Read the maximum size for each group

result1 = CalculateMaxItems(tot1, gro)  # Calculate for the first set
result2 = CalculateMaxItems(tot2, gro)  # Calculate for the second set

print(result1 * result2)  # Output the final result
