"""Building a tool to translate between bases"""

def rebase(input_base, digits, output_base):
    """Convert a sequence of digits in one base, representing a number, into a sequence         of digits in another base, representing the same number."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    n = len(digits)
    calculation = []
    for each_number in digits:
        if each_number < 0 or each_number >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        formula = each_number * input_base**(n-1)
        n -= 1
        calculation.append(formula)

    decimal_value = sum(calculation)

    if decimal_value == 0:
        return [0]
    
    result = []
    while decimal_value > 0:
        remainder = decimal_value % output_base
        result.append(remainder)
        decimal_value //= output_base
        
    result.reverse()
    return result