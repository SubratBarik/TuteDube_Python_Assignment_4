"""
This program writes in the file by taking user end data and also appends few more lines to it.
"""
# file where we have to add user data and append few more line(s)
file = "output.txt"

user_input = input("Enter text to write to the file: ")

with open(file, "tw") as fh:
    fh.write(user_input + "\n")
    print(f"Data successfully written to {file}")

try:
    addon_input = input("Enter additional text to append: ")
    with open(file, "a") as fh:
        fh.write(addon_input + "\n")
        print(f"Data successfully appended to {file}")
except Exception as e:
    print(f"Error: {e}")

print(f"\nFinal content of {file}")
with open(file, "r") as fh:
    print(fh.read())



