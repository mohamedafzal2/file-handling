try:
    # Attempt to add two numbers
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a + b  # Perform the addition
    print("The result is:", result)

except ValueError:
    # Handle the case where the inputs are not numbers
    print("Error: Both inputs must be valid numbers.")

finally:
    # Print a message regardless of whether an exception was raised or not
    print("Addition operation complete.")
