"""Determind if a number is perfect/abundant/deficient based on Aliquot Sum formula"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Category 1: Perfect
    # Define which are the factors of the "number"
    
    factor = []
    for num in range(1, number):
        if number % num == 0:
            factor.append(num)
        else:
            continue

    aliquot_sum = sum(factor)

    if number == aliquot_sum:
        return "perfect"
    elif number < aliquot_sum:
        return "abundant"
    elif number > aliquot_sum:
        return "deficient"
    return None