def rgb_to_hex(rgb):
    #xd
    """Convert RGB tuple to hexadecimal color code."""
    r, g, b = rgb
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


rgb_color = (255, 128, 0)
hex_color = rgb_to_hex(rgb_color)
print("RGB:", rgb_color)
print("Hex:", hex_color)

