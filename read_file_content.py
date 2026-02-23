"""
This program reads the file content by handling file not found error

Note: we can achieve it by two ways using error handling:
a) print(fh.read())
b) for loop
"""

# file from where we need to read the contents
file = "sample.txt"

try:
    with open(file, "tr") as fh:
        #print(fh.read())
        # or
        for line in fh:
            print(line.strip())
except FileNotFoundError:
        print(f"Error: The file {file} was not found")