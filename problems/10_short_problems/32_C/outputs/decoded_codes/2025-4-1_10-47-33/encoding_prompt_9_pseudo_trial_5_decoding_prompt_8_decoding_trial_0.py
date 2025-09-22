def calculate_modified_quantity(quantity, divisor):
    total_units = quantity // divisor
    remainder = quantity % divisor
    if remainder > 0:
        return remainder * (total_units + 1)
    else:
        return quantity

quantity_a = int(input())
quantity_b = int(input())
divisor = int(input())

modified_quantity_a = calculate_modified_quantity(quantity_a, divisor)
modified_quantity_b = calculate_modified_quantity(quantity_b, divisor)

final_result = modified_quantity_a * modified_quantity_b
print(final_result)


   def calculate_modified_quantity(quantity: int, divisor: int) -> int:
   

   if divisor == 0:
       raise ValueError("Divisor cannot be zero.")
   