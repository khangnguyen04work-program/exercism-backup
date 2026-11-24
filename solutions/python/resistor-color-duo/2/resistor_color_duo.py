"""A program that take color names as input and output a two digit number, even if the input is more than two colors"""

# Global variable
color_list = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

def value(colors):
    """Function to find two digit number from the given color(s)"""
    
    convert_list = []
    for color in colors:
        corresponding_index = color_list.index(color)
        convert_list.append(str(corresponding_index))
        
    if len(convert_list) > 2:
        convert_list.pop()

    result = "".join(convert_list)
    return int(result)
        
