def normalizePath(filePath):
    # Here you would implement actual logic to normalize the path
    # One possible normalization can involve removing redundant elements
    # For simplicity, let's just return the input in this example
    nor = filePath.replace("//", "/").replace("./", "").strip()  # Example normalization; more logic can be added
    return nor


def removeExtraLeadingSlashes(filePath):
    # Ensure the path starts with exactly one slash: removing extra slashes
    if filePath.startswith("/"):
        modifiedPath = "/" + filePath.lstrip("/")
    else:
        modifiedPath = filePath  # No changes if there are no leading slashes
    return modifiedPath


# Step 1: Read input from standard input
ra = input()  # Input the file path

# Step 2: Normalize the file path
nor = normalizePath(ra)

# Step 3: Ensure the path starts with a single forward slash
if nor.startswith("/"):
    red = removeExtraLeadingSlashes(nor)
else:
    red = nor  # If there are no leading slashes, keep it as is

# Step 4: Print the final result
print(red)
