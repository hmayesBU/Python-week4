def test_function(num1, num2):
    """
    Function to demonstrate how a function works, and how it is used.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.

    Returns:
    result: The result of the sum of the inputs
        - int or float

    Example Usage:
    --------------
    test_function(4, 5)  # Output: 9
    test_function(10.5, 2.5)  # Output: 13

    """

    print("The first number is: ", num1)
    print("The second number is: ", num2)

    result = num1 + num2
    print(result)

    return result

#This is outside of the function - you can call it here>>
print(test_function(1,2))
print(test_function(1.5,2.6))
print(test_function(100000,2232564684))
print(test_function(-11,2))
print(test_function(1.3,2)

            