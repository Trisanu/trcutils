import PIL.Image as pImage

# ascii characters used to build the output text
ASCII_CHARS = [ "@" , "#" , "$" , "%" , "?" , "*" , "+" , ":" , "," , "."]

# resize image according to new width
def resize_image(image, new_width = 375):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

# convert picels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//30] for pixel in pixels])
    return characters


def main(new_width = 375):

    # attempt to open image from user-input

    mypath = input("Enter a valid pathname to an image:\n")
    
    try:
        inp_image = pImage.open(mypath)
    
        # convert image to ASCII
        new_image_data = pixels_to_ascii(grayify(resize_image(inp_image)))

        # format
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i : (i + new_width)] for i in range(0, pixel_count, new_width))

        # print result
        print(ascii_image)

        # save result to ascii_image.txt
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)

    except:
        print(mypath, "is not a valid path to an image")


main()
