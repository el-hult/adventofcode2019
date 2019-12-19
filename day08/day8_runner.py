from day8_lib import compute_checksum, render_image, BLACK

IMAGE_WIDTH = 25
IMAGE_TALL = 6

with open('inputs/day8.txt', 'r') as f:
    MY_INPUT = f.readline().strip()

checksum_a = compute_checksum(IMAGE_TALL, IMAGE_WIDTH, MY_INPUT)
print(f"The checksum of the image is {checksum_a}")

image_data = render_image(IMAGE_TALL,IMAGE_WIDTH,MY_INPUT)
image_string = "\n".join(
    map(
        lambda row: "".join(
            map(lambda pixel_value: "o" if pixel_value == BLACK else " ",
                row, )
        ),
        image_data,)
)
print("The password for the Rover BIOS is given byt the password in the image render below:")
print(image_string)