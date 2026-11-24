"""Create a prgram that looks up the numerical value associated with a particular color band"""

def color_code(color):
    """Find the proper index corresponding with the color in a specific order"""
    
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue",                            "violet", "grey", "white"]
    if color in color_list:
        index_in_color_list = color_list.index(color)
        corresponding_values = index_in_color_list
        return corresponding_values
    return None
        
def colors():
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue",                            "violet", "grey", "white"]
    return color_list
