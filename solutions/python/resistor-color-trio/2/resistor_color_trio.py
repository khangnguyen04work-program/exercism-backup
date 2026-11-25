"""Function to find value in ohms"""

# Global Variable
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

def label(colors):
    """Add corresponding numbers of zeros after index 2 of converted_list, then remove the index 2 value. Join every added zeros to 2 first index values!"""
    converted_list = []

    for color in colors[:3]:
        corresponding_value = color_list.index(color)
        converted_list.append(str(corresponding_value))
        continue
        
    number_of_zeros = 0
    while number_of_zeros < int(converted_list[2]):
        converted_list.append("0")
        number_of_zeros += 1
        continue

    converted_list.pop(2)
    
    result = "".join(converted_list)

    if converted_list.count("0") < 3:
        return f"{int(result)} ohms"
    if converted_list.count("0") == 3 or 3 < converted_list.count("0") < 6:
        result = result[:-3]
        return f"{int(result)} kiloohms"
    if converted_list.count("0") == 6 or 6 < converted_list.count("0") < 9:
        result = result[:-6]
        return f"{int(result)} megaohms"
    if converted_list.count("0") == 9:
        result = result[:-9]
        return f"{int(result)} gigaohms"
    return None