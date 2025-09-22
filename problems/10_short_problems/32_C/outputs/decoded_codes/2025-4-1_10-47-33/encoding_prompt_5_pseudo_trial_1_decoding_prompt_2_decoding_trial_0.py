# Define the function to adjust quantity
def AdjustQuantity(TotalCount, StepSize):
    Quotient = TotalCount // StepSize  # Integer division to get the whole number
    Remainder = TotalCount % StepSize   # Modulus to get the leftover part

    if Remainder > 0:
        return (Quotient + 1) * Remainder  # Adjust the quantity if there's remainder
    else:
        return TotalCount  # Return the total count if no adjustment is needed

# Read input values
FirstValue, SecondValue, StepSize = map(int, input().split())  # Read and convert to integers

# Calculate adjusted values
AdjustedFirstValue = AdjustQuantity(FirstValue, StepSize)
AdjustedSecondValue = AdjustQuantity(SecondValue, StepSize)

# Output the final product
print(AdjustedFirstValue * AdjustedSecondValue)
