"""Producing a sentence using the given name and the given number as a ordinal numeral"""

def line_up(name, number):
    """Function to filter 1 digit condition and 2&3 digits conditions (the given number is expected to be in a range between 1 and 999"""
    
    while number in range(1, 1000):
        # 1 digit condition:
        if number == 1:
            return f"{name}, you are the {number}st customer we serve today. Thank you!"
        if number == 2:
            return f"{name}, you are the {number}nd customer we serve today. Thank you!"
        if number == 3:
            return f"{name}, you are the {number}rd customer we serve today. Thank you!"
        if 3 < number < 10:
            return f"{name}, you are the {number}th customer we serve today. Thank you!"
        # 2 & 3 digits condition:
        digits = []
        for digit in str(number):
            digits.append(digit)

        special_handler = "".join(digits)
        
        if digits[-1] == "1" and special_handler != "11" and special_handler[-2:] != "11":
            return f"{name}, you are the {number}st customer we serve today. Thank you!"
        if digits[-1] == "2" and special_handler != "12" and special_handler[-2:] != "12":
            return f"{name}, you are the {number}nd customer we serve today. Thank you!"
        if digits[-1] == "3" and special_handler != "13" and special_handler[-2:] != "13":
            return f"{name}, you are the {number}rd customer we serve today. Thank you!"
        return f"{name}, you are the {number}th customer we serve today. Thank you!"