"""
    This file can help you that how can you write the recursive programs -in mathematics- with python.
    We have these for now:
        Factorial
        Sum of numbers from 1 to n
        Power/Exponent
"""


def factorial(number: int) -> int:
    """
        Calculate the factorial of a non-negative integer.

        Args:
            number (int): The non-negative integer whose factorial is to be calculated.

        Returns:
            int: The factorial of the input integer.

        Raises:
            ValueError: If the input is negative.

        Example:
            factorial(4) -> 4*3*2*1
    """
    
    result = 0

    if number == 0 or number == 1:
        return 1
    elif number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        result = number * factorial(number-1)
        return result

def sum_of_numbers_from_one_to_n(number: int) -> int:
    """
        Calculate the sum of numbers from one to `n` of a non-negative integer.

        Args:
            number (int): The non-negative integer whose number is to be calculated.

        Returns:
            int: The result of the sum of numbers from 1 to `n` integer.

        Raises:
            ValueError: If the input is negative.

        Example:
            sum_of_numbers_from_one_to_n(4) -> 4+3+2+1
    """

    result = 0

    if number == 0 or number == 1:
        return 1
    elif number < 0:
        raise ValueError("This function is not defined for negative numbers.")
    else:
        result = number + sum_of_numbers_from_one_to_n(number-1)
        return result

def power(base: int, exponent: int) -> int:
    """
        Calculate the power/exponent of a non-negative integer.

        Args:
            number (int): The non-negative integer whose number is to be calculated for exponent.

        Returns:
            int: The power of the input integer.

        Raises:
            ValueError: If the input is negative.

        Example:
            power(4) -> 4*4*4*4
    """

    result = 0

    if exponent == 1:
        return base
    else:
        result = base * power(base, exponent-1)
        return result
