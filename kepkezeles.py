from PIL import Image


def split_image(image_path, width, height):
    try:
        # Open the image
        img = Image.open(image_path)
        # Get the dimensions of the original image
        img_width, img_height = img.size

        # Calculate the number of smaller images in horizontal and vertical directions
        num_horizontal = img_width // width
        num_vertical = img_height // height

        # Iterate through each smaller image
        for i in range(num_vertical):
            for j in range(num_horizontal):
                # Calculate the coordinates for cropping
                left = j * width
                upper = i * height
                right = left + width
                lower = upper + height

                # Crop the image
                cropped_img = img.crop((left, upper, right, lower))

                # Save the cropped image
                cropped_img.save(f"cropped_image_{i}_{j}.png")

        print("Image successfully split!")

    except Exception as e:
        print("An error occurred:", e)


# Example usage
split_image("input_image.jpg", 100, 100)
