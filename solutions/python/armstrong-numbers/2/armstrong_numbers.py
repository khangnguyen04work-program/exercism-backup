def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    number_of_digits = len(digits)
    each_digit_result = []
    for digit in digits:
        powered_digit = digit ** number_of_digits
        each_digit_result.append(powered_digit)
    total = sum(each_digit_result)
    return total == number