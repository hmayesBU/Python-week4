number = int(input("Enter a number: "))

# Convert the number to a string and count the characters
num_digits = len(str(abs(number)))

print(f"The number {number} has {num_digits} digits.")
