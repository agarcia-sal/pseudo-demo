def AdjustQuantity(TotalCount, StepSize):
    Quotient = TotalCount // StepSize
    Remainder = TotalCount % StepSize
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


   def AdjustQuantity(TotalCount, StepSize):
       """Adjust quantity based on its divisibility by StepSize."""
   

   try:
       FirstValue, SecondValue, StepSize = map(int, input().split())
       if StepSize == 0:
           raise ValueError("StepSize cannot be zero.")
   except ValueError as e:
       print(e)
       exit(1)
   