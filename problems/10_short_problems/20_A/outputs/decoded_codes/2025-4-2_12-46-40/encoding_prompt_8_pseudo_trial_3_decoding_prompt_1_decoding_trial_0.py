import os

# Step 1: Read input
original_path = input()
trimmed_path = original_path.strip()

# Step 2: Normalize the file path
normalized_path = os.path.normpath(trimmed_path)

# Step 3: Ensure the path starts with a single forward slash
final_path = "/" + normalized_path.lstrip("/")

# Step 4: Output the final result
print(final_path)
