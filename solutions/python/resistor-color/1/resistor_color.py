def color_code(color):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue",                            "violet", "grey", "white"]
    if color in color_list:
        index_in_color_list = color_list.index(color)
        corresponding_values = index_in_color_list
        return corresponding_values
        
def colors():
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue",                            "violet", "grey", "white"]
    return color_list
