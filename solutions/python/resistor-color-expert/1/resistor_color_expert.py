"""Translate resistor color bands into a formatted resistance and tolerance label."""

COLOR_LIST = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def format_value(value):
    """Return an integer if the scaled value has no decimal part, otherwise a float."""
    return int(value) if value.is_integer() else value


def resistor_label(colors):
    """Return the resistance value, metric prefix, and tolerance for 1, 4, or 5 bands."""
    if len(colors) == 1:
        return "0 ohms"

    base_value = 0
    for color in colors[:-2]:
        base_value = base_value * 10 + COLOR_LIST.index(color)

    multiplier = 10 ** COLOR_LIST.index(colors[-2])
    ohms = base_value * multiplier
    tolerance = TOLERANCE[colors[-1]]

    if ohms >= 1_000_000_000:
        scaled = format_value(ohms / 1_000_000_000)
        return f"{scaled} gigaohms ±{tolerance}"
    if ohms >= 1_000_000:
        scaled = format_value(ohms / 1_000_000)
        return f"{scaled} megaohms ±{tolerance}"
    if ohms >= 1_000:
        scaled = format_value(ohms / 1_000)
        return f"{scaled} kiloohms ±{tolerance}"

    return f"{ohms} ohms ±{tolerance}"