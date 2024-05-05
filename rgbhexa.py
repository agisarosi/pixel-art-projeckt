def rgb_to_hex(rgb_color):
    # Check if the RGB values are within the valid range
    for color in rgb_color:
        if color < 0 or color > 255:
            raise ValueError("RGB values must be between 0 and 255")

    # Convert RGB to hexadecimal
    hex_color = "#{:02X}{:02X}{:02X}".format(rgb_color[0], rgb_color[1], rgb_color[2])

    return hex_color

# Example usage
rgb_color = (255, 69, 0)
hex_color = rgb_to_hex(rgb_color)
print("Hexadecimal:", hex_color)
