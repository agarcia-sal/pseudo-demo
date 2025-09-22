def AdjustQuantity(TotalCount, StepSize):
    # Calculate the quotient and remainder when TotalCount is divided by StepSize
    Quotient = TotalCount // StepSize
    Remainder = TotalCount % StepSize
    
    # Check if there is a remainder and return accordingly
    if Remainder > 0:
        return Remainder * (Quotient + 1)  # Adjust quantity based on remainder
    else:
        return TotalCount  # Return original TotalCount if no adjustment is needed

# Read input values from the user
FirstValue = int(input())
SecondValue = int(input())
StepSize = int(input())

# Calculate adjusted values using the AdjustQuantity function
AdjustedFirstValue = AdjustQuantity(FirstValue, StepSize)
AdjustedSecondValue = AdjustQuantity(SecondValue, StepSize)

# Calculate and output the final product of adjusted values
final_product = AdjustedFirstValue * AdjustedSecondValue
print(final_product)
