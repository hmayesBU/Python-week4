"""
Function to allow demonstration of how to run a function
"""

def test_function(num1, num2):
    """
    Lots of metadata in here to tell you all about the function
    it wil be over many lines
    """

    print("The first number is: ", num1)
    print("The second number is: ", num2)

    result = num1 + num2
    print(result)

    return result

#This is outside of the function - you can call it here>>
print(test_function(1,2))
print(test_function(2.6,2.0))
print(test_function(3,2.6))
print(test_function(859,-262))
            