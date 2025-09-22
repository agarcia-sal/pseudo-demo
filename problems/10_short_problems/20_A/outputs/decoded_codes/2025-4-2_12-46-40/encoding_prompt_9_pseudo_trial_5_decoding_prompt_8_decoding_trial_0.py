import os

# Step 1: Read Input
file_path = input()

# Step 2: Normalize the File Path
normalized_path = os.path.normpath(file_path)

# Step 3: Remove Leading Slashes
if normalized_path.startswith("/"):
    normalized_path = "/" + normalized_path.lstrip("/")

# Step 4: Output the Final Path
print(normalized_path)


   def normalize_file_path(input_path):
       normalized_path = os.path.normpath(input_path)
       if normalized_path.startswith("/"):
           normalized_path = "/" + normalized_path.lstrip("/")
       return normalized_path
   