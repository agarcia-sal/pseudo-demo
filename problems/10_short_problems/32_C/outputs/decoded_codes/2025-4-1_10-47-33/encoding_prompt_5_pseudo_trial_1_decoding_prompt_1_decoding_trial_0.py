def AdjustQuantity(TotalCount, StepSize):
    Quotient = TotalCount // StepSize  # Integer division for the whole number quotient
    Remainder = TotalCount % StepSize    # Modulus operation for remainder
    
    if Remainder > 0:
        return Remainder * (Quotient + 1)
    else:
        return TotalCount

# Read input values
FirstValue, SecondValue, StepSize = map(int, input().split())

# Calculate adjusted values
AdjustedFirstValue = AdjustQuantity(FirstValue, StepSize)
AdjustedSecondValue = AdjustQuantity(SecondValue, StepSize)

# Calculate and output the final product
print(AdjustedFirstValue * AdjustedSecondValue)
