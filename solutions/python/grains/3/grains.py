def square(number):
    """Find the number of grains on a specific square number"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
        
# Test: square(4)
# Though process: 1st = 1 -> 2nd = 1 * 2 -> 3rd = 2 * 2 -> 4nd = 4 * 2

def total():
    """Find the total of grains on the chessboard by summing up number of grains in each square together"""
    total_grains = []
    for chessboard_position in range(1,65): # There are 64 squares in total on the chessboard
        grain_on_square = 2**(chessboard_position - 1)
        total_grains.append(grain_on_square)
    return sum(total_grains)

print(total())