"""Functions to help cooking a gorgeous lasagna."""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining time for baking.

    Parameter:
        elapsed_bake_time: int - baking time already elapsed
        
    Return: 
        int: remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time with the assigned number of layers.

    Parameters
        number_of_layers: int - number of lasagna layers.
        
    Return: 
    int total preparation time (in minutes) assuming each layer takes 2 mins.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time has been elapsing.

    Paramerters
        number_of_layers: int - number of lasagna layers.
        elapsed_bake_time: int - baking time already elapsed.
        
    Return: int - total elapsed time (prepping + baking) in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time